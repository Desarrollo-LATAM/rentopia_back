from django import forms
from django.contrib.auth.models import User

from .models import MessageModel


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ["sender", "receiver", "message_content"]
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=200)
    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email', 
            'password'                 
        ]
