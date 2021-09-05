from django import forms
from django.forms import fields, models
from .models import Contact_Form

class Con_Form(forms.ModelForm):
    class Meta:
        model=Contact_Form
        fields="__all__"
