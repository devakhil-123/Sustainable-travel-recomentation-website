from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BicycleModel




class LogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())




class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]


class BicycleForm(forms.ModelForm):
    class Meta:
        model=BicycleModel
        fields="__all__"
        widgets={
            "yourname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter name"}),
            "youremail":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}),
            "yourmessage":forms.Textarea(attrs={"class":"form-control","placeholder":"enter message"})
        }