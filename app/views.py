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
        li=request.POST.get('link')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data.img1=img 
        data.tittle=na
        data.discription=des
        data.link=li
        data.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/EDIT.html",{'data':data})
def brandedit(request,id):
    data1=tble1.objects.get(id=id)
    if request.method=='POST':
        na=request.POST.get('tittle1')
        des=request.POST.get('discription1')
        li=request.POST.get('link')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data1.img2=img 
        data1.tittle1=na
        data1.discription1=des
        data1.link=li
        data1.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/brandedit.html",{'data1':data1})
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
        li=request.POST.get('link')
        data1=tble1.objects.create(tittle1=ta1,img2=im2,discription1=di1,link=li)
        return HttpResponseRedirect(reverse('DETAIL'))
        # data1.save()
    return render(request,"app/home.html",{})
def sliders(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im1=request.FILES['image1']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=tble.objects.create(tittle=ta,img1=im1,discription=di,link=li)
        return HttpResponseRedirect(reverse('sliders'))
    url = "http://127.0.0.1:8000/home/sliders"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    # response1= urllib.request.urlopen(url1)
    # data1 = json.loads(response1.read())
    context={'data':data}
    return render(request,"app/sliders.html",context) 
    # return render(request,"app/sliders.html",{})
    # url = "http://127.0.0.1:8000/tble"
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/sliders.html",{'data':data}) 
def brands(request):
    if request.method=='POST':
        ta1=request.POST.get('tittle1')
        im2=request.FILES['image2']
        di1=request.POST.get('discription1')
        li=request.POST.get('link')
        data1=tble1.objects.create(tittle1=ta1,img2=im2,discription1=di1,link=li)
        return HttpResponseRedirect(reverse('brands'))
    url1 = "http://127.0.0.1:8000/home/brands"
    response1= urllib.request.urlopen(url1)
    data1 = json.loads(response1.read())
    context={'data1':data1}
    return render(request,"app/brands.html",context) 
    # data1.save()
    # return render(request,"app/brands.html",{})  
def stunningproject(request):
        if request.method=='POST':
            ta=request.POST.get('tittle')
            im=request.FILES['image']
            di=request.POST.get('discription')
            li=request.POST.get('link')
            data=projects.objects.create(tittle=ta,img=im,discription=di,link=li)
            return HttpResponseRedirect(reverse('stunningproject'))
        url = "http://127.0.0.1:8000/home/projects" 
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return render(request,"app/stunningproject.html",{'data':data})
def recentblogposts(request):
        if request.method=='POST':
            ta=request.POST.get('tittle')
            im=request.FILES['image']
            di=request.POST.get('discription')
            li=request.POST.get('link')
            data=blogs.objects.create(tittle=ta,img=im,discription=di,link=li)
            return HttpResponseRedirect(reverse('recentblogposts'))
        url = "http://127.0.0.1:8000/home/blogs" 
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return render(request,"app/recentblogposts.html",{'data':data})
def service(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=service.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('service'))
    return render(request,"app/service.html",{})
def blogedit(request,id):
    data=blogs.objects.get(id=id)
    if request.method=='POST':
        na=request.POST.get('tittle')
        des=request.POST.get('discription')
        li=request.POST.get('link')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data.img=img 
        data.tittle=na
        data.discription=des
        data.link=li
        data.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/blogedit.html",{'data':data})
def projectedit(request,id):
    data=projects.objects.get(id=id)
    if request.method=='POST':
        na=request.POST.get('tittle')
        des=request.POST.get('discription')
        li=request.POST.get('link')
        if 'Image' in request.FILES: 
            img=request.FILES["Image"]
            data.img=img 
        data.tittle=na
        data.discription=des
        data.link=li
        data.save()
        return HttpResponseRedirect(reverse('home'))   
    return render(request,"app/projectedit.html",{'data':data})
def delete(request,id):
    data=projects.objects.get(id=id).delete()
    data1=projects.objects.all()
    return HttpResponseRedirect(reverse('stunningproject'))
def blogdelete(request,id):
    data=blogs.objects.get(id=id).delete()
    data1=blogs.objects.all()
    return HttpResponseRedirect(reverse('recentblogposts'))
def brandelete(request,id):
    data=tble1.objects.get(id=id).delete()
    data=tble1.objects.all()
    return HttpResponseRedirect(reverse('brands')) 
def slidedelete(request,id):
    data=tble.objects.get(id=id).delete()
    data=tble.objects.all()
    return HttpResponseRedirect(reverse('sliders'))   