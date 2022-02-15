from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from second_app.models import Order
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"