from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


Workout_level= [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advance', 'Advance'),
    
    ]

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    country=forms.CharField(max_length=20)
    age=forms.IntegerField()
    height=forms.IntegerField()
    weight=forms.IntegerField()
    workout= forms.CharField(label='Choose your workout level?', widget=forms.Select(choices=Workout_level))







    class Meta:
        model=User
        fields=['username','email','password1','password2',
        'country','age','height','weight']