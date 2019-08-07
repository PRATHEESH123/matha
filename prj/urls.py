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
    url(r'^stunningproject/$',stunningproject,name='stunningproject'),
    url(r'^DETAIL/$',DETAIL,name='DETAIL'),
    url(r'^sliderdetails/EDIT/(?P<id>[0-9]+)',EDIT,name='EDIT'),
    url(r'^sliderdetails/EDIT/$',sliders,name='sliders'),
    url(r'^service/$',service,name='service'),
    url(r'^services/$',services,name='services'),
    url(r'^branddetails/$',brands,name='brands'),
    url(r'^recentblogposts/$',recentblogposts,name='recentblogposts'),
    # url(r'^ourtestimonials/$',ourtestimonials,name='ourtestimonials'),
    url(r'^promotions/$',promotions,name='promotions'),
    url(r'^careers/$',careers,name='careers'),
    url(r'^fun/$',fun,name='fun'),
    url(r'^home/sliders/(?P<id>[0-9]+)', views.tbleList.as_view()),
    url(r'^home/sliders/', views.Listtble.as_view()),
    url(r'^home/brands/(?P<id>[0-9]+)', views.tble1List.as_view()),
    url(r'^home/brands/',views.Listtble1.as_view()),
    url(r'^home/projects/(?P<id>[0-9]+)', views.projectList.as_view()),
    url(r'^home/projects/', views.project.as_view()),
    url(r'^home/blogs/(?P<id>[0-9]+)', views.blogsList.as_view()),
    url(r'^home/blogs/', views.blog.as_view()),
    url(r'^brandedit/(?P<id>[0-9]+)',brandedit,name='brandedit'),
    url(r'^blogedit/(?P<id>[0-9]+)',blogedit,name='blogedit'),
    url(r'^projectedit/(?P<id>[0-9]+)',projectedit,name='projectedit'),
    url(r'^delete/(?P<id>[0-9]+)',delete,name='delete'),
    url(r'^brandelete/(?P<id>[0-9]+)',brandelete,name='brandelete'),
    url(r'^blogdelete/(?P<id>[0-9]+)',blogdelete,name='blogdelete'),
    url(r'^slidedelete/(?P<id>[0-9]+)',slidedelete,name='slidedelete'),
    url(r'^$',home,name='home'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
