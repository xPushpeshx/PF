from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from website.models import Contact 
from django.shortcuts import redirect


def home(request):
    if request.method=="POST":
        ip=getipadd(request)
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if len(name)<2 or len(email)<8 :
            return render(request,'home.html',{'message_name':name})
        else:
            ex=Contact(ip=ip,name=name,email=email,subject=subject,message=message)
            send_mail(
                'subject',
                "Name: " + name + "\n Email: " + email + "\n MESSAGE : "+ message +'\n IPA :' + ip ,
                'email',
                ['sagarpushpesh@outlook.com'],
                fail_silently=False,
            )
            ex.save()
            return render(request,'home.html',{})
    return render(request,'home.html')

def getipadd(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipa = x_forwarded_for.split(',')[0]
    else:
        ipa = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ipa
def donate(request):
    return redirect('https://p.paytm.me/xCTH/5b8f2678')