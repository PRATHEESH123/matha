from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
from app1.views import *
from app1.serializers import *
import urllib.request
import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required

# Create your views here.

#home functions:
@login_required
def home(request):
    return render(request,"app/home.html",{})
@login_required
def backimages(request):
    if request.method=='POST':
        im1=request.FILES['Brandimg']
        im2=request.FILES['Blogimg']
        im3=request.FILES['Projectimg']
        im4=request.FILES['Knowusimg']
        im5=request.FILES['Serviceimg']
        im6=request.FILES['Whatweimg']
        im7=request.FILES['Careersimg']
        im8=request.FILES['Aboutusimg']
        im9=request.FILES['Contactusimg']
        data=backgroundimages.objects.create(Brandimg=im1,Blogimg=im2,Projectimg=im3,Knowusimg=im4,Serviceimg=im5,Whatweimg=im6,Careersimg=im7,Aboutusimg=im8,Contactusimg=im9)
        return HttpResponseRedirect(reverse('backimages'))
    # url = "http://127.0.0.1:8000/backgroundimages/"
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # # data=backgroundimages.objects.all()
    # # import pprint
    # # pprint.pprint(data)
    # return render(request,"app/backimages.html",{'data': data})
    queryset =backgroundimages.objects.all()
    serializer_class = backgroundimagesSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/backimages.html",context)


@login_required
def imgdelete(request,id):
    data=backgroundimages.objects.get(id=id).delete()
    data1=backgroundimages.objects.all()
    return HttpResponseRedirect(reverse('backimages'))
    
@login_required
def imgedit(request,id):
    data=backgroundimages.objects.get(id=id)
    if 'Image' in request.FILES:
        im1=request.FILES["Image"]
        data.Brandimg=im1
        data.save()
        return HttpResponseRedirect(reverse('home'))
    if 'Image1' in request.FILES: 
        im2=request.FILES["Image1"]
        data.Blogimg=im2
        data.save()
        return HttpResponseRedirect(reverse('home')) 
    if 'Image2' in request.FILES: 
        im3=request.FILES["Image2"]
        data.Projectimg=im3
        data.save()
        return HttpResponseRedirect(reverse('home'))
    if 'Image3' in request.FILES: 
        im4=request.FILES["Image3"]
        data.Knowusimg=im4
        data.save()
        return HttpResponseRedirect(reverse('home'))
    if 'Image4' in request.FILES: 
        im5=request.FILES["Image4"]
        data.Serviceimg=im5
        data.save()
        return HttpResponseRedirect(reverse('home')) 

    if 'Image5' in request.FILES: 
        im6=request.FILES["Image5"]
        data.Whatweimg=im6
        data.save()
        return HttpResponseRedirect(reverse('home'))

    if 'Image6' in request.FILES: 
        im7=request.FILES["Image6"]
        data.Careersimg=im7
        data.save()
        return HttpResponseRedirect(reverse('home'))

    if 'Image7' in request.FILES: 
        im8=request.FILES["Image7"]
        data.Aboutusimg=im8
        data.save()
        return HttpResponseRedirect(reverse('home'))

    if 'Image8' in request.FILES: 
        im9=request.FILES["Image8"]
        data.Contactusimg=im9
        data.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,"app/imgedit.html",{'data':data})

    # if 'Image' in request.FILES: 
    #     im1=request.FILES['Brandimg']
    #     im2=request.FILES['Blogimg']
    #     im3=request.FILES['Projectimg']
    #     im4=request.FILES['Knowusimg']
    #     im5=request.FILES['Serviceimg']
    #     im6=request.FILES['Whatweimg']
    #     im7=request.FILES['Careersimg']
    #     im8=request.FILES['Aboutusimg']
    #     im9=request.FILES['Contactusimg']
    #     data.Brandimg=im1
    #     data.Blogimg=im2
    #     data.Projectimg=im3
    #     data.Knowusimg=im4
    #     data.Serviceimg=im5
    #     data.Whatweimg=im6
    #     data.Careersimg=im7
    #     data.Aboutusimg=im8
    #     data.Contactusimg=im9
    #     data.save()
    #     return HttpResponseRedirect(reverse('home'))   
    # return render(request,"app/imgedit.html",{'data':data})
@login_required
def sliders(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im1=request.FILES['image1']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=tble.objects.create(tittle=ta,img1=im1,discription=di,link=li)
        return HttpResponseRedirect(reverse('sliders'))
    # url = "http://127.0.0.1:8000/home/sliders"
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # context={'data':data}
    
    queryset =tble.objects.all()
    serializer_class = tbleSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/sliders.html",context)




@login_required
def brands(request):
    if request.method=='POST':
        ta1=request.POST.get('tittle1')
        im2=request.FILES['image2']
        di1=request.POST.get('discription1')
        li=request.POST.get('link')
        data1=tble1.objects.create(tittle1=ta1,img2=im2,discription1=di1,link=li)
        return HttpResponseRedirect(reverse('brands'))
    url1 = "http://mathagroup.herokuapp.com/home/brands/"
    response1= urllib.request.urlopen(url1)
    data1 = json.loads(response1.read())
    context={'data1':data1}
    return render(request,"app/brands.html",context)
    # queryset=tble1.objects.all()
    # serializer_class =tble1Serializer(queryset, many =True)
    # context={'data':serializer_class.data}
    # return render(request,"app/brands.html",context)



@login_required    
def stunningproject(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=projects.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('stunningproject'))
    # url = "http://127.0.0.1:8000/home/projects" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/stunningproject.html",{'data':data})
    queryset =projects.objects.all()
    serializer_class = projectsSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/stunningproject.html",context)

@login_required    
def recentblogposts(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=blogs.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('recentblogposts'))
    # url = "http://127.0.0.1:8000/home/blogs" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/recentblogposts.html",{'data':data})

    queryset =blogs.objects.all()
    serializer_class = blogsSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/recentblogposts.html",context)


#Edit functions
@login_required
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
@login_required    
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
@login_required    
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
@login_required    
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

#Delete functions:
@login_required
def delete(request,id):
    data=projects.objects.get(id=id).delete()
    data1=projects.objects.all()
    return HttpResponseRedirect(reverse('stunningproject'))
@login_required    
def blogdelete(request,id):
    data=blogs.objects.get(id=id).delete()
    data1=blogs.objects.all()
    return HttpResponseRedirect(reverse('recentblogposts'))
@login_required   
def brandelete(request,id):
    data=tble1.objects.get(id=id).delete()
    data=tble1.objects.all()
    return HttpResponseRedirect(reverse('brands')) 
@login_required    
def slidedelete(request,id):
    data=tble.objects.get(id=id).delete()
    data=tble.objects.all()
    return HttpResponseRedirect(reverse('sliders'))

#Service Functions:
@login_required
def services(request):
   return render(request,"app/services.html",{})
@login_required   
def abcdef(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=service.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('abcdef'))
    # url = "http://127.0.0.1:8000/services/service" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/service.html",{'data':data})

    queryset =service.objects.all()
    serializer_class = serviceSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/service.html",context)


#Service edit function:
@login_required
def aaa(request,id):
    data=service.objects.get(id=id)
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
    return render(request,"app/servicedit.html",{'data':data})

#Service delete function:
@login_required
def servicedelete(request,id):
    data=service.objects.get(id=id).delete()
    data=service.objects.all()
    return HttpResponseRedirect(reverse('abcdef'))

#Promotion functions:
@login_required
def prom(request):
    return render(request,"app/promotions.html",{})
@login_required    
def ghijkl(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=promotions.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('our'))
    # url = "http://127.0.0.1:8000/promotions/promotionals/" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/ourpromotions.html",{'data':data})

    queryset =promotions.objects.all()
    serializer_class=promotionsSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/ourpromotions.html",context)

#promotion edit function:
@login_required
def bbb(request,id):
    data=promotions.objects.get(id=id)
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
    return render(request,"app/promoedit.html",{'data':data})

# promotions delete function:
@login_required
def promodelete(request,id):
    data=promotions.objects.get(id=id).delete()
    data=promotions.objects.all()
    return HttpResponseRedirect(reverse('our'))
@login_required    
def contact(request):
    return render(request,"app/contact.html",{})
@login_required
def ab(request):
    return render(request,"app/about.html",{})
@login_required    
def ggggg(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=about.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('ffff'))
    # url = "http://127.0.0.1:8000/about/aboutus/" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/aboutus.html",{'data':data})

    queryset =about.objects.all()
    serializer_class =aboutSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/aboutus.html",context)

@login_required
def yyyy(request,id):
    data=about.objects.get(id=id)
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
    return render(request,"app/aboutedit.html",{'data':data})
@login_required    
def aboutdelete(request,id):
    data=about.objects.get(id=id).delete()
    data=about.objects.all()
    return HttpResponseRedirect(reverse('ffff'))
@login_required    
def ourteam(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=team.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('ourteam'))
    # url = "http://127.0.0.1:8000/about/ourteam/" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/ourteam.html",{'data':data})

    queryset =team.objects.all()
    serializer_class =teamSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/ourteam.html",context)

@login_required    
def teamedit(request,id):
    data=team.objects.get(id=id)
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
    return render(request,"app/teamedit.html",{'data':data})
@login_required
def teamdelete(request,id):
    data=team.objects.get(id=id).delete()
    data=team.objects.all()
    return HttpResponseRedirect(reverse('ourteam'))


@login_required    
def wwww(request):
    return render(request,"app/careers.html",{})
@login_required
def opportunity(request):
    if request.method=='POST':
        ta=request.POST.get('tittle')
        im=request.FILES['image']
        di=request.POST.get('discription')
        li=request.POST.get('link')
        data=careers.objects.create(tittle=ta,img=im,discription=di,link=li)
        return HttpResponseRedirect(reverse('rrrr'))
    # url = "http://127.0.0.1:8000/careers/opportunity/" 
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    # return render(request,"app/opportunity.html",{'data':data})

    queryset =careers.objects.all()
    serializer_class =careersSerializer(queryset, many =True)
    context = {'data':serializer_class.data}
    return render(request,"app/opportunity.html",context)


@login_required
def opredit(request,id):
    data=careers.objects.get(id=id)
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
    return render(request,"app/opredit.html",{'data':data})
@login_required
def oprdelete(request,id):
    data=careers.objects.get(id=id).delete()
    data=careers.objects.all()
    return HttpResponseRedirect(reverse('rrrr'))
def index(request):
    return render(request,"app/index.html",{})
def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # else:
        #     # messages.info(request, "Invalid USer")
        #     return redirect('register')
@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')

def usercontact(request):
    # msg=""
    if request.method=="POST":
        na=request.POST.get('t1')
        em=request.POST.get('t2')
        su=request.POST.get('t3')
        ms=request.POST.get('t4')
        data=contact_tble.objects.create(name=na,email=em,subject=su,message=ms)
        # msg="Message successfully sent!!"
        return HttpResponseRedirect(reverse('usercontact'))
    return render(request,"app/ucontact.html")
@login_required
def contactus(request):
    data=contact_tble.objects.all()
    return render(request,"app/contactus.html",{'data': data})