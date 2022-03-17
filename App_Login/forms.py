from django import forms
from django.contrib.auth.forms import UserCreationForm
from App_Login.models import User, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields=('email','password1','password2',)