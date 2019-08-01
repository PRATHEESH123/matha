from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
from app1.views import *
import urllib.request
import json 

# Create your views here.

def DETAIL(request):
    # data=tble.objects.all()
    # data1=tble1.objects.all()
    url = "http://127.0.0.1:8000/tble"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    url1 = "http://127.0.0.1:8000/tble1"
    response1= urllib.request.urlopen(url1)
    data1 = json.loads(response1.read())
    context={'data':data,'data1':data1}
    return render(request,"app/DETAIL.html",context) 
def careers(request):
    return render(request,"app/careers.html",{})
def EDIT(request,id):
    data=tble.objects.get(id=id)
    if request.method=='POST':
        na=request.POST.get('tittle')
        des=request.POST.get('discription')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data.img1=img 
        data.tittle=na
        data.discription=des
        data.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/EDIT.html",{'data':data})
def home(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im1=request.FILES['image1']
        di=request.POST.get('discription')
        # ta1=request.POST.get('tittle1')
        # di1=request.POST.get('discription1')
        # im2=request.POST.get('image2')
        data=tble.objects.create(tittle=ta,img1=im1,discription=di)
        #data1=tble1.objects.create(tittle1=ta1,discription1=di1,img2=im2)
        # data.save()
        return HttpResponseRedirect(reverse('DETAIL'))
    return render(request,"app/home.html",{})
def promotions(request):
    return render(request,"app/promotions.html",{})
def services(request):
    return render(request,"app/services.html",{})
def fun(request):
    if request.method=='POST':
        ta1=request.POST.get('tittle1')
        im2=request.FILES['image2']
        di1=request.POST.get('discription1')
        data1=tble1.objects.create(tittle1=ta1,img2=im2,discription1=di1)
        return HttpResponseRedirect(reverse('DETAIL'))
        # data1.save()
    return render(request,"app/home.html",{})
def new(request,id):
    data1=tble1.objects.get(id=id)
    if request.method=='POST':
        na1=request.POST.get('tittle1')
        des1=request.POST.get('discription1')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data1.img2=img 
        data1.tittle1=na1
        data1.discription1=des1
        data1.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/EDIT.html",{'data1':data1})    





