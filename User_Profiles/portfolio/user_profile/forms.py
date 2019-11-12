from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    """
    This form class is using Django Admin User Model's
    fields, we also add new fields in it 'password'
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """
    form class using UserProfileInfo model created in models.py
    this has one-to-one relation with User Model
    """
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class EditProfileForm(UserChangeForm):
    """
    This form is inherit from Django Auth Forms
    to change user password
    """
    class Meta:
        model = User
        fields = ('email', 'first_name',
                  'last_name', 'password')

