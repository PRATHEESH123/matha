from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import tble
from app.models import tble1
from app.models import projects
from app.models import blogs
from app1.serializers import tbleSerializer
from app1.serializers import tble1Serializer
from app1.serializers import projectsSerializer
from app1.serializers import blogsSerializer

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