"""adbk URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import register
from .import api
from .import database

urlpatterns = [
    path('admin/', admin.site.urls),

     path('register',register.registration),
     path('login/',register.Login),
     path('index',register.CheckLogin),
     path('contact',api.contact),
     #path('contactus',database.contactus),
     path('food/',api.tiffin),
     path('aboutus/',api.aboutus),
     path('book/',api.book),
     path('booknow',database.booknow),
     path('cinema/',api.cinema),
     path('hospital/',api.hospital),
     path('order/',api.order),
     path('rooms/',api.rooms),
     path('school/',api.school),
     path('shops/',api.shops),
]
