"""prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from app.views import *
from app1.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home,name='home'),
    url(r'^DETAIL/$',DETAIL,name='DETAIL'),
    url(r'^EDIT/(?P<id>[0-9]+)',EDIT,name='EDIT'),
    url(r'^services/$',services,name='services'),
    url(r'^promotions/$',promotions,name='promotions'),
    url(r'^careers/$',careers,name='careers'),
    url(r'^fun/$',fun,name='fun'),
    url(r'^tble/', views.tbleList.as_view()),
    url(r'^tble1/', views.tble1List.as_view()),
    url(r'^new/(?P<id>[0-9]+)',new,name='new'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

