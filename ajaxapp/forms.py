from  django import forms
from django.core import validators
from django.forms import widgets 
from .models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('name', 'price','pages',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'id':'price'}),
            'pages': forms.TextInput(attrs={'class':'form-control', 'id':'pages'}),
        }

