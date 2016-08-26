from django import forms
from django.forms import ModelForm
from .models import User, Tweet

class RegisterForm(ModelForm):
    class Meta:
        pass
           

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['user_name', 'password', 'email']
            
class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet']