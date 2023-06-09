from django import forms
from emailandsmsapp.models import RegModel
class RegForm(forms.Form):
    FirstName=forms.CharField(max_length=10)
    LastName=forms.CharField(max_length=10)
    UserName=forms.CharField(max_length=10)
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput())
    CPassword=forms.CharField(max_length=10,widget=forms.PasswordInput())
    Emailid=forms.EmailField()
    MobileNo=forms.CharField(max_length=10)