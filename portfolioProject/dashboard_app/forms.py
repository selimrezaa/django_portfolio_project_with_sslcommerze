from django import forms
from second_app.models import *
from dashboard_app.models import Feedback

from django.contrib.auth.models import User


class AddSlider(forms.ModelForm):
    class Meta:
        model = HomePageTopSlider
        fields = "__all__"


class AddHOmePageComplete(forms.ModelForm):
    class Meta:
        model = HomePageWeComplete
        fields = "__all__"


class AddYouCanGet(forms.ModelForm):
    class Meta:
        model = HomePageYouGet
        fields = "__all__"


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "img", "phone", "country", "city", "zip_code")


class AddAchivement(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = "__all__"


class AddFooter(forms.ModelForm):
    class Meta:
        model = Footer
        fields = "__all__"


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password", "is_active", "is_staff")


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["password", "groups", "first_name", "last_name"]


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ProductBasicForm(forms.ModelForm):
    class Meta:
        model = BasicProduct
        fields = "__all__"


class ProductStanderdForm(forms.ModelForm):
    class Meta:
        model = StanderdProduct
        fields = "__all__"


class ProductProForm(forms.ModelForm):
    class Meta:
        model = ProProduct
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['star', 'message']
