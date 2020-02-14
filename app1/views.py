from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from app.models import tble
from app.models import tble1
from app.models import projects
from app.models import blogs
from app.models import service
from app.models import promotions
from app.models import about
from app.models import team
from app.models import careers
from app.models import backgroundimages
from app1.serializers import backgroundimagesSerializer
from app1.serializers import tbleSerializer
from app1.serializers import tble1Serializer
from app1.serializers import projectsSerializer
from app1.serializers import blogsSerializer
from app1.serializers import serviceSerializer
from app1.serializers import aboutSerializer
from app1.serializers import teamSerializer
from app1.serializers import careersSerializer
from app1.serializers import brandSerializer
from app1.serializers import blogSerializer
from app1.serializers import projectSerializer
from app1.serializers import knowusSerializer
from app1.serializers import serSerializer
from app1.serializers import whatSerializer
from app1.serializers import carSerializer
from app1.serializers import aboutSerializer
from app1.serializers import contaSerializer

# Create your views here.

class tbleList(APIView):
    def get(self,request,id):
        tble1=tble.objects.filter(id=id) 
        serializer=tbleSerializer(tble1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
    
class Listtble(APIView):
    def get(self,request):
        tble1=tble.objects.all() 
        serializer=tbleSerializer(tble1,many=True)
        return Response(serializer.data)       

class tble1List(APIView):
    def get(self,request,id):
        tble2=tble1.objects.filter(id=id)
        serializer=tble1Serializer(tble2,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Listtble1(APIView):    
    def get(self,request):
        tble2=tble1.objects.all()
        serializer=tble1Serializer(tble2,many=True)
        return Response(serializer.data)

class project(APIView):
    def get(self,request):
        proj=projects.objects.all()
        serializer=projectsSerializer(proj,many=True)
        return Response(serializer.data)

class projectList(APIView):
    def get(self,request,id):
        proj=projects.objects.filter(id=id)
        serializer=projectsSerializer(proj,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class blog(APIView):         
    def get(self,request):
        blg=blogs.objects.all()
        serializer=blogsSerializer(blg,many=True)
        return Response(serializer.data)

class blogsList(APIView):
    def get(self,request,id):
        blg=blogs.objects.filter(id=id)
        serializer=blogsSerializer(blg,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class servi(APIView):         
    def get(self,request):
        ser=service.objects.all()
        serializer=serviceSerializer(ser,many=True)
        return Response(serializer.data)

class serviList(APIView):
    def get(self,request,id):
        ser=service.objects.filter(id=id)
        serializer=serviceSerializer(ser,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class promotionalapi(APIView):         
    def get(self,request):
        pro=promotions.objects.all()
        serializer=serviceSerializer(pro,many=True)
        return Response(serializer.data)

class promotionalapiList(APIView):
    def get(self,request,id):
        pro=promotions.objects.filter(id=id)
        serializer=serviceSerializer(pro,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class aboutapi(APIView):         
    def get(self,request):
        abu=about.objects.all()
        serializer=serviceSerializer(abu,many=True)
        return Response(serializer.data)

class aboutapiList(APIView):
    def get(self,request,id):
        abu=about.objects.filter(id=id)
        serializer=serviceSerializer(abu,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class teamapi(APIView):         
    def get(self,request):
        abu=team.objects.all()
        serializer=serviceSerializer(abu,many=True)
        return Response(serializer.data)

class teamapiList(APIView):
    def get(self,request,id):
        abu=team.objects.filter(id=id)
        serializer=serviceSerializer(abu,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class careersapi(APIView):         
    def get(self,request):
        abu=careers.objects.all()
        serializer=careersSerializer(abu,many=True)
        return Response(serializer.data)

class careersapiList(APIView):
    def get(self,request,id):
        abu=careers.objects.filter(id=id)
        serializer=careersSerializer(abu,many=True)
        return Response(serializer.data)
    def post(self):
        pass 

class backgroundimgApi(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=backgroundimagesSerializer(imm,many=True)
        return Response(serializer.data)

class backgroundimgApiList(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.filter(id=id)
        serializer=backgroundimagesSerializer(imm,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class listbrands(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=brandSerializer(imm, many=True)
        return Response(serializer.data)

class listbrandslist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=brandSerializer(imm)
        return Response(serializer.data['Brandimg'])

    def post(self):
        pass

class listblogs(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=blogSerializer(imm,many=True)
        return Response(serializer.data)

class listblogslist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=blogSerializer(imm)
        return Response(serializer.data['Blogimg'])

    def post(self):
        pass

class listproject(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=projectSerializer(imm,many=True)
        return Response(serializer.data)

class listprojectlist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=projectSerializer(imm)
        return Response(serializer.data['Projectimg'])

    def post(self):
        pass


class listknowus(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=knowusSerializer(imm,many=True)
        return Response(serializer.data)

class listknowuslist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=knowusSerializer(imm)
        return Response(serializer.data['Knowusimg'])

    def post(self):
        pass

class listservice(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=serSerializer(imm,many=True)
        return Response(serializer.data)

class listservicelist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=serSerializer(imm)
        return Response(serializer.data['Serviceimg'])

    def post(self):
        pass

class listwhat(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=whatSerializer(imm,many=True)
        return Response(serializer.data)

class listwhatlist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=whatSerializer(imm)
        return Response(serializer.data['Whatweimg'])

    def post(self):
        pass

class listcar(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=carSerializer(imm,many=True)
        return Response(serializer.data)

class listcarlist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=carSerializer(imm)
        return Response(serializer.data['Careersimg'])

    def post(self):
        pass

class listabout(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=aboutSerializer(imm,many=True)
        return Response(serializer.data)

class listaboutlist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=aboutSerializer(imm)
        return Response(serializer.data['Aboutusimg'])

    def post(self):
        pass

class listcontact(APIView):
    def get(self,request):
        imm=backgroundimages.objects.all()
        serializer=contaSerializer(imm,many=True)
        return Response(serializer.data)

class listcontactlist(APIView):
    def get(self,request,id):
        imm=backgroundimages.objects.get(id=id)
        serializer=contaSerializer(imm)
        return Response(serializer.data['Contactusimg'])

    def post(self):
        pass
