from django import forms
from .models import *



class RecordForm(forms.ModelForm):
    success_url = 'contact'
    class Meta:
        model = record
        fields = ['name', 'number', 'message']