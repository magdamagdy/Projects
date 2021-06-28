from django import forms
from .models import Additem

class AdditemForm(forms.ModelForm):
    class Meta:
        model = Additem
        fields = ('image', 'description', 'price', 'amount', 'category')
