from django.shortcuts import render, redirect

from .models import Emfood
from .forms import Emfoodadd

def index(request):
    foodData = Emfood.objects.all()
    header = ['ID', '非常食名', '保有数', '消費期限']
    my_dict = {
        'title': '保有非常食一覧',
        'header': header,
        'foodData': foodData,
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