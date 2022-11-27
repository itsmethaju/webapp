
from dataclasses import fields

from django import forms
from .models import Contact, Subscribe

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','comments',]
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class SubForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email',]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            
        }