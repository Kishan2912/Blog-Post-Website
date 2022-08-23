from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from .models import profile

class userregistionform(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class userupdateform(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class Profileupdateform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image']