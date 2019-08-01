from rest_framework import serializers
from app.models import tble
from app.models import tble1

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