from rest_framework import serializers
from app.models import tble
from app.models import tble1
from app.models import projects
from app.models import *


class tbleSerializer(serializers.ModelSerializer):
    class Meta:
        model=tble
        fields='__all__'
        
class tble1Serializer(serializers.ModelSerializer):
     class Meta:
         model=tble1
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

class serviceSerializer(serializers.ModelSerializer):

    class Meta:
        model=service
        fields=('tittle','img')
        fields='__all__'

class promotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=promotions
        fields='__all__'

class aboutSerializer(serializers.ModelSerializer):

    class Meta:
        model=about
        fields=('tittle','img')
        fields='__all__'
    
class teamSerializer(serializers.ModelSerializer):

    class Meta:
        model=team
        fields=('tittle','img')
        fields='__all__'
    
class careersSerializer(serializers.ModelSerializer):

    class Meta:
        model=careers
        fields=('tittle','img')
        fields='__all__'
    
class backgroundimagesSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields='__all__'

class brandSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Brandimg',)
        # fields='__all__'

class blogSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Blogimg',)


class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Projectimg',)

class knowusSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Knowusimg',)

class serSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Serviceimg',)

class whatSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Whatweimg',)

class carSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Careersimg',)

class aboutSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Aboutusimg',)
    

class contaSerializer(serializers.ModelSerializer):

    class Meta:
        model=backgroundimages
        fields=('Contactusimg',)
