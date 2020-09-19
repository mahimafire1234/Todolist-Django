from django import forms
from .models import *

class Form_todo(forms.ModelForm):

    class Meta:
        model=Task
        fields="__all__"