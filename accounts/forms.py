from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)