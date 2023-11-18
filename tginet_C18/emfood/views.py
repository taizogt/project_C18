from django.shortcuts import render

from .models import Emfood

def index(request):
    foodData = Emfood.objects.all()
    header = ['ID', '非常食名', '保有数', '消費期限']
    my_dict = {
        'title': '保有非常食一覧',
        'header': header,
        'foodData': foodData,
    }
    return render(request, "emfood/index.html", my_dict)