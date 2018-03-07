from django import forms
from django.contrib.auth.forms import UserCreationForm
from foodfeed.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="")
    last_name = forms.CharField(max_length=30, required=False, help_text="")
    email = forms.EmailField(max_length=254, help_text="")


    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class LogInForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")