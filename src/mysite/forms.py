from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32)
    email = forms.CharField(required=True, label='Email', max_length=32)
    password = forms.CharField(required=True, label='Password', max_length=32,
                               widget=forms.PasswordInput())


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )
        exclude = ('password',)

    def clean_password(self):
        return ""
