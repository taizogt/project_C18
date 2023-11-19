from django import forms
from .models import Emfood  # importに追加
from django.forms import widgets, NumberInput  # importに追加

class Emfoodadd(forms.ModelForm):
    class Meta:
        model = Emfood
        fields = ['name','num','expire_date']
        # expire_dateをプルダウン式に変更
        widgets = {
            'expire_date': NumberInput(attrs={'type': 'date'})
        }
