from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import tble
from app.models import tble1
from app1.serializers import tbleSerializer
from app1.serializers import tble1Serializer


# Create your views here.

class tbleList(APIView):

    def get(self,request):
        tble1=tble.objects.all() 
        serializer=tbleSerializer(tble1,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class tble1List(APIView):

    def get(self,request):
        tble2=tble1.objects.all() 
        serializer=tble1Serializer(tble2,many=True)
        return Response(serializer.data)
    def post(self):
        pass
