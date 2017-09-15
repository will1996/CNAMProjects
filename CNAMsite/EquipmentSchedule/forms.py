from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 help_text='required, used to identify you!')
    last_name = forms.CharField(max_length=30,
                                help_text='required, used to identify you!')
    email = forms.EmailField(max_length=254,
                             help_text='Required.Input a valid email address.')


class meta:
    model = User
    fields = fields = ('username', 'email', 'password1', 'password2', )
