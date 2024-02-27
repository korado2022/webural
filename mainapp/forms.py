from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = PhoneNumberField()
    company = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
