from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from website.models import Contact 


def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if len(name)<2 or len(email)<8 :
            return render(request,'home.html',{'message_name':name})
        else:
            ex=Contact(name=name,email=email,subject=subject,message=message)
            ex.save()
            send_mail(
                name,
                message,
                email,
                ['sagarpushpesh@outlook.com'],
                fail_silently=False,
            )
            return render(request,'home.html',{})
    return render(request,'home.html')