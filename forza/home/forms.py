from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput())
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='email',widget=forms.EmailInput())
    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='пароль', widget=forms.PasswordInput())
    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ('email', 'password')

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='email', widget=forms.EmailInput())
    content = forms.CharField(label='Контент', widget=forms.Textarea())
    captcha = CaptchaField()


