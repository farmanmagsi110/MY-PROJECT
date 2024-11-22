from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo 
        fields = ["name" , "password" , "age"]
        widgets = {
            "password" : forms.PasswordInput(),
            
        }