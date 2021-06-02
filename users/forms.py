from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text='You will receive a copy of your report if you provide an email.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


