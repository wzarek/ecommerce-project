from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstName', 'lastName', 'email', 'message')
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'imie'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'nazwisko'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'twoja wiadomość'}),
        }