from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"homepage/home.html")

def login(request):
    return render(request,"homepage/login.html")

def create(request):
    return render(request,"tasks/create.html")


def index(request):
    # return HttpResponse("Hey welcome here")
    task=Task.objects.all()
    form=Form_todo()
    if request.method=="POST":
        form=Form_todo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/create')
    return render(request,"tasks/landing.html",{'task':task,'form':form})

def update(request,pk):
    task=Task.objects.get(id=pk)
    form=Form_todo(instance=task)

    if request.method=="POST":
        form=Form_todo(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect("/create")
    return render(request,"tasks/Update.html",{'form':form})

def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect("/create")