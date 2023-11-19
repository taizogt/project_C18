from django.shortcuts import render, redirect

from .models import Emfood
from .forms import Emfoodadd
from django.utils import timezone

def index(request):
    # expire_dateをlimit_dateに変更お願いします
    foodData = Emfood.objects.all().order_by('limit_date')
    header = ['ID', '非常食名', '保有数', '消費期限']
    todays_date = timezone.now().date()
    month_later_1 = todays_date + timezone.timedelta(days=30)
    # foodData内でtodays_dateよりもlimit_dateが前のものの個数をきろく
    outdata = 0
    for food in foodData:
        if food.limit_date < todays_date:
            outdata += 1
    month1_data = 0
    for food in foodData:
        if (food.limit_date < month_later_1) & (food.limit_date > todays_date):
            month1_data += 1
    my_dict = {
        'title': '保有非常食一覧',
        'header': header,
        'foodData': foodData,
        'now': todays_date,
        'month_later_1': month_later_1,
        'out': outdata,
        'near': month1_data,
    }
    return render(request, "emfood/index.html", my_dict)

def register(request):
    message = ''
    
    if(request.method == 'POST'):
        form = Emfoodadd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/emfood')
        else:
            message = '登録に失敗しました'
    
    modelform_dict = {
        'title': '非常食登録',
        'form': Emfoodadd(),
        'message': message,
    }
    return render(request, "emfood/register.html", modelform_dict)

# シェア一覧画面のメソッド
def share(request):
    foodData = Emfood.objects.filter(shere=1).order_by('limit_date')
    header = ['ID', '非常食名', '保有数', '消費期限']
    my_dict = {
        'title': '保有非常食一覧',
        'header': header,
        'foodData': foodData,
    }
    return render(request, "emfood/share.html", my_dict)

# index.htmlでシェアするボタンを押した時に動くメソッド
def sharefood(request, id):
    
    message = ''
    emfood_obj=Emfood.objects.get(id=id)
    if (request.method=='POST'):
        emfood_obj.shere=1
        emfood_obj.save()
    
    return render(request,"emfood/share")

def delete(request, id):
    header = ['ID', '非常食名', '保有数', '消費期限']
    message = ''
    emfood_obj = Emfood.objects.get(id=id)
    if (request.method == 'POST'):
        emfood_obj.delete()
        return redirect(to='/emfood')
    delete_dict = {
        'title': '削除画面',
        'header': header,
        'id': id,
        'emfood': emfood_obj,
        'message': message,
    }
    return render(request, "emfood/index.html", delete_dict)
    
