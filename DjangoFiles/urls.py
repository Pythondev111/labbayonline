"""DjangoFiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from DjangoFiles import settings
from Myfiles.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('maxsulotlar/',maxsulotlar,name='maxsulotlar'),
    path('biz_haqimizda/',about,name='about'),
    path('bog`lanish',boglanish,name='boglansh'),
    path('savatcha/',korzinka,name='korzinka'),
    path('signin/',signin,name='signin'),
    path('anketa/',anketa,name='anketa'),
    path('delete/<str:id>/',deletee,name='delete'),

    path('login/',loginn ,name='loginn'),
    path('logout/',logoutt,name='logout'),
    path('single/<str:id>/',single,name='single')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIAFILES_DIRS)