from .models import Emfood  # importに追加
...

class Emfoodadd(forms.ModelForm):
    class Meta:
        model = Emfood
        fields = ['name','num','expire_date']
