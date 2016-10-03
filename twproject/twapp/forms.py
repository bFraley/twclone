from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from .models import Member, Tweet
from . import views


class PostingForm(forms.ModelForm):
    msg = forms.CharField(max_length=140)
    
    class Meta:
        model = Tweet
        fields = ('msg',)


class LoginForm(AuthenticationForm):
    pass

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('account',)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2',)


    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
