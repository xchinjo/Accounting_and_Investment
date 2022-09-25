import email
from email import message
from django.shortcuts import render

from aai_project.aaiapp.models import AiModel

def home(request):
    if request.method=="POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        m = request.POST.get("message")
        data = AiModel(name=na, email=em, phone=ph, message=m)
        data.save()
        return render(request, "home.html")
    else:
        return render(request, "home.html")
