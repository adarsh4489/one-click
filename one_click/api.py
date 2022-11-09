from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def tiffin(request):
    return render(request,'food.html',{'msg':''})

def contact(request):
    return render(request,'contact.html',{'msg':''})

def aboutus(request):
    return render(request,'Aboutus.html',{'msg':''})

def book(request):
    return render(request,'booknow.html',{'msg':''})


def cinema(request):
    return render(request,'cinemahall.html',{'msg':''})


def hospital(request):
    return render(request,'hospital.html',{'msg':''})

def order(request):
    return render(request,'order.html',{'msg':''})

def register(request):
    return render(request,'register.html',{'msg':''})

def rooms(request):
    return render(request,'rooms.html',{'msg':''})

def school(request):
    return render(request,'school.html',{'msg':''})

def shops(request):
    return render(request,'shops.html',{'msg':''})