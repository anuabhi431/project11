from django.shortcuts import render
from django.views import View
import requests
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from project11.settings import EMAIL_HOST_USER
from .forms import RegForm
from .models import RegModel
# Create your views here.
class Home(View):
    def get(self,request):
        rf=RegForm()
        con_dic={'rf':rf}
        return render(request,'home.html',context=con_dic)
class Reg(View):
    def post(self,request):
        otp=str(random.randint(100000000,999999990))
        print(otp)
        mobno=request.POST["MobileNo"]
        emailid=request.POST["Emailid"]
        resp = requests.post('https://textbelt.com/text', {
            'phone': mobno,
            'message': otp,
            'key': '4709b7e6dea07f2863e7dcc78359b9c3fa687db3eyGCXKXhQnYZbaS2zBkHtu5J1',
        })
        print(resp.json())
        send_mail("otp for registration",otp,EMAIL_HOST_USER,[emailid],fail_silently=True)
        rf=RegForm(request.POST)
        if rf.is_valid():
            rm=RegModel(FName=rf.cleaned_data["FirstName"],
                        LName=rf.cleaned_data["LastName"],
                        UName=rf.cleaned_data['UserName'],
                        Password=rf.cleaned_data['Password'],
                        CPassword=rf.cleaned_data['CPassword'],
                        Email=rf.cleaned_data['Emailid'],
                        Mobo=rf.cleaned_data['MobileNo'])
            rm.save()
            return HttpResponse("reg success");


# Create your views here.


# Create your views here.
