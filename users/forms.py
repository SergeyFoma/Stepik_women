from django import forms
from django.contrib.auth.forms import AuthenticationForm

# class LoginUserForm(forms.Form):
class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label="login", widget=forms.TextInput(attrs={"class":"form-input"}))
    password=forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-input"}))


