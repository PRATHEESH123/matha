from rest_framework import serializers
from app.models import tble
from app.models import tble1
from app.models import projects
from app.models import blogs

class tbleSerializer(serializers.ModelSerializer):

    class Meta:
        model=tble
        fields=('tittle','img1')
        fields='__all__'

class tble1Serializer(serializers.ModelSerializer):

     class Meta:
         model=tble1
         fields=('tittle1','img2')
         fields='__all__'

class projectsSerializer(serializers.ModelSerializer):

    class Meta:
        model=projects
        fields=('tittle','img')
        fields='__all__'

class blogsSerializer(serializers.ModelSerializer):

    class Meta:
        model=blogs
        fields=('tittle','img')
        fields='__all__'
        