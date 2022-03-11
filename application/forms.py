from django import forms
from application.models import pro
from django.core import validators


class productpage(forms.ModelForm):
    class Meta:
        model = pro
        fields = ['item_name','price','desc','img']
        widgets = {
            'item_name':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.NumberInput(attrs={'class': 'form-control'}),
            'desc':forms.Textarea(attrs={'class': 'form-control'}),
            'img':forms.FileInput(attrs={'class': 'form-control'}),
            
        }