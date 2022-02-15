from django.forms import fields, widgets
from .models import ContactModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Your Name *"}),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':"Your Phone Number *"}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':"Your Email *"}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':"Your Message *",'style':"width: 100%; height: 150px;"})
        }


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user