from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegisterUser(UserCreationForm):
    choices = (
        ( '8-15','8-15'),
    ('15-25','15-25'),
    ('25-40','25-40'),
    ('40-55','40-55'),
    (  '55+','55+')
    )
    tel = forms.CharField(max_length=15)
    yosh = forms.ChoiceField(choices=choices)
    email = forms.EmailField()



    class Meta:
        model = User
        fields = ['username','tel','yosh','email']
