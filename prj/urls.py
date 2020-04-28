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
    url(r'^$',index,name='index'),
    url(r'^login',login,name='login'),
    url(r'^logout',logout, name='logout'),


    # home ulrs:
    url(r'^home$',home,name='home'),
    url(r'^sliderdetails/EDIT/$',sliders,name='sliders'),
    url(r'^branddetails/$',brands,name='brands'),
    url(r'^recentblogposts/$',recentblogposts,name='recentblogposts'),
    url(r'^stunningproject/$',stunningproject,name='stunningproject'),
    url(r'^backimages$',backimages,name='backimages'),
    url(r'^imgedit/edit(?P<id>[0-9]+)',imgedit,name='imgdit'),
    url(r'^imgdelete/(?P<id>[0-9]+)',imgdelete,name='imgdelete'),


    # Home/edit urls:
    url(r'^sliderdetails/EDIT/(?P<id>[0-9]+)',EDIT,name='EDIT'),
    url(r'^brandedit/(?P<id>[0-9]+)',brandedit,name='brandedit'),
    url(r'^blogedit/(?P<id>[0-9]+)',blogedit,name='blogedit'),
    url(r'^projectedit/(?P<id>[0-9]+)',projectedit,name='projectedit'),

    #Home/delete urls:
    url(r'^delete/(?P<id>[0-9]+)',delete,name='delete'),
    url(r'^brandelete/(?P<id>[0-9]+)',brandelete,name='brandelete'),
    url(r'^blogdelete/(?P<id>[0-9]+)',blogdelete,name='blogdelete'),
    url(r'^slidedelete/(?P<id>[0-9]+)',slidedelete,name='slidedelete'),

    #Home/API/ urls:
    url(r'^home/sliders/(?P<id>[0-9]+)', views.tbleList.as_view()),
    url(r'^home/sliders/', views.Listtble.as_view()),
    url(r'^home/brands/(?P<id>[0-9]+)', views.tble1List.as_view()),
    url(r'^home/brands/',views.Listtble1.as_view()),
    url(r'^home/projects/(?P<id>[0-9]+)', views.projectList.as_view()),
    url(r'^home/projects/', views.project.as_view()),
    url(r'^home/blogs/(?P<id>[0-9]+)', views.blogsList.as_view()),
    url(r'^home/blogs/', views.blog.as_view()),


    #Service urls:
    url(r'^services$',services,name='services'),
    url(r'^ourservices/$',abcdef,name='abcdef'),

    #Service edit urls:
    url(r'^servicedit/(?P<id>[0-9]+)',aaa,name='servedit'),

    #service delete urls:
    url(r'^servicedelete/(?P<id>[0-9]+)',servicedelete,name='servicedelete'),


    #Service/API/urls:
    url(r'^services/service/(?P<id>[0-9]+)', views.serviList.as_view()),
    url(r'^services/service/', views.servi.as_view()),


    #Promotion urls:

    url(r'^promotions$',prom,name='promotions'),
    url(r'^ourpromotions/$',ghijkl,name='our'),


    #Promotional API urls:
    url(r'^promotions/promotionals/(?P<id>[0-9]+)', views.promotionalapiList.as_view()),
    url(r'^promotions/promotionals/', views.promotionalapi.as_view()),  
    
    #promotion edit urls:
    url(r'^promoedit/(?P<id>[0-9]+)',bbb,name='bbb'),

    #promotion delete urls:
    url(r'^promodelete/(?P<id>[0-9]+)',promodelete,name='promodelete'),
    url(r'^careers$',wwww,name='careers'),
    url(r'^opportunity/$',opportunity,name='rrrr'),
    url(r'^contact$',contact,name='contact'),
    #About urls:
    url(r'^about$',ab,name='hhhh'),
    url(r'^aboutus/$',ggggg,name='ffff'),

    #About edit urls:
    url(r'^editabout/(?P<id>[0-9]+)',yyyy,name='aboutedit'),

    #About delete urls:
    url(r'^aboutdelete/(?P<id>[0-9]+)',aboutdelete,name='aboutdelete'),

    #About API urls:
    url(r'^about/aboutus/(?P<id>[0-9]+)', views.aboutapiList.as_view()),
    url(r'^about/aboutus/', views.aboutapi.as_view()), 
    url(r'^ourteam/$',ourteam,name='ourteam'),

    #team API urls:
    url(r'^about/ourteam/(?P<id>[0-9]+)', views.teamapiList.as_view()),
    url(r'^about/ourteam/', views.teamapi.as_view()), 
    url(r'^teamdelete/(?P<id>[0-9]+)',teamdelete,name='teamdelete'),

    #carrier API urls:
    url(r'^careers/opportunity/(?P<id>[0-9]+)', views.careersapiList.as_view()),
    url(r'^careers/opportunity/', views.careersapi.as_view()), 

    url(r'^careers/edit(?P<id>[0-9]+)',opredit,name='opredit'),
    url(r'^careers/delete/(?P<id>[0-9]+)',oprdelete,name='oprdelete'),

    url(r'^teamedit/(?P<id>[0-9]+)',teamedit,name='teamedit'),
    url(r'^contactus/$',contactus,name='ccc'),
    url(r'^usercontact',usercontact,name='usercontact'),

    url(r'^backgroundimages/(?P<id>[0-9]+)', views.backgroundimgApiList.as_view()),
    url(r'^backgroundimages/', views.backgroundimgApi.as_view()),

    url(r'^backgroundimage/brand/(?P<id>[0-9]+)', views.listbrandslist.as_view()),
    url(r'^backgroundimage/brand/', views.listbrands.as_view()),

    url(r'^backgroundimage/blog/(?P<id>[0-9]+)', views.listblogslist.as_view()),
    url(r'^backgroundimage/blog/', views.listblogs.as_view()),


    url(r'^backgroundimage/project/(?P<id>[0-9]+)', views.listprojectlist.as_view()),
    url(r'^backgroundimage/project/', views.listproject.as_view()),

    url(r'^backgroundimage/listknows/(?P<id>[0-9]+)', views.listknowuslist.as_view()),
    url(r'^backgroundimage/listknows/', views.listknowus.as_view()),

    url(r'^backgroundimage/service/(?P<id>[0-9]+)', views.listservicelist.as_view()),
    url(r'^backgroundimage/service/', views.listservice.as_view()),

    url(r'^backgroundimage/whatweprovide/(?P<id>[0-9]+)', views.listwhatlist.as_view()),
    url(r'^backgroundimage/whatweprovide/', views.listwhat.as_view()),

    url(r'^backgroundimage/careers/(?P<id>[0-9]+)', views.listcarlist.as_view()),
    url(r'^backgroundimage/careers/', views.listcar.as_view()),

    url(r'^backgroundimage/about/(?P<id>[0-9]+)', views.listaboutlist.as_view()),
    url(r'^backgroundimage/about/', views.listabout.as_view()),

    url(r'^backgroundimage/contact/(?P<id>[0-9]+)', views.listcontactlist.as_view()),
    url(r'^backgroundimage/contact/', views.listcontact.as_view()),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
