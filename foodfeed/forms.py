from django import forms
from django.contrib.auth.forms import UserCreationForm
from foodfeed.models import User, Picture, Comment


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))
    last_name = forms.CharField(max_length=30, required=False, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))
    email = forms.EmailField(max_length=254, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class LogInForm(forms.ModelForm):
    email = forms.EmailField(max_length=254 , widget=forms.TextInput(attrs={'class': "indexForm"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "indexForm"}))

    class Meta:
        model = User
        fields = ("email", "password")


class ImageUploadForm(forms.ModelForm):
    picture = forms.ImageField(label="Select a picture" )

    class Meta:
        model = Picture
        fields = ("picture", "description")


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="First Name: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))
    last_name = forms.CharField(max_length=30, required=False, help_text="Last Name: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))
    email = forms.EmailField(max_length=254, help_text="Email Address: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))

    class Meta:
        model = User
        fields = ("avatar", "first_name", "last_name", "email")


class CommentSubmissionForm(forms.ModelForm):
    comment = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': "commentInput"}))

    class Meta:
        model = Comment
        fields = ("comment", "picture")
