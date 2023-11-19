from django import forms
from .models import Emfood  # importに追加
from django.forms import widgets, NumberInput  # importに追加

class Emfoodadd(forms.ModelForm):
    class Meta:
        model = Emfood
        fields = ['name','num','limit_date','user']
        # expire_dateをプルダウン式に変更
        widgets = {
            'limit_date': NumberInput(attrs={'type': 'date'}),
            'user': widgets.HiddenInput()
        }
        labels = {
            'name': '非常食名',
            'num': '登録個数',
            'limit_date': '消費期限',
        }
