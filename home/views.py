from django.shortcuts import render
from home.models import task,contactuser
# Create your views here.
def index(request):
    context = {'success':False }
    if request.method == "POST":
        tasktitle=request.POST['tasktitle']
        taskdescripion=request.POST['taskdescription']
        detail=task(Task = tasktitle , Task_Description = taskdescripion )
        detail.save()
        context = {'success' : True, 'msg1':'congratulations','msg2':'Your task is added'}
    elif request.method == "GET":
        context = {'success' : False, 'msg1':'Welcome','msg2':'Welcome to our website'}

    return render(request, 'index.html' , context)
def contact(request):
    context={'success':False , 'msg1':'Hey' , 'msg2':"Have querry? Contact Us"}
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        address=request.POST['address']
        description=request.POST['description']
        contactuserdetail=contactuser(Name=name , Address = address , Description=description , Email=email)
        contactuserdetail.save()
        context={'success':False , 'msg1':'Thank You' , 'msg2':name+", we will let you soon."}
    return render(request, 'contact.html' ,context)
def about(request):
    return render(request, 'index.html')
def task1(request):
    alltask=task.objects.all()
    context = {'tasks':alltask}
    return render(request, 'tasklist.html' ,context)
# def submit(request):
    
