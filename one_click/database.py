from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def contactus(request):
    try:
        db,cmd=pool.ConnectionPooling()
        fullname=request.POST['fullname']
        emailaddres=request.POST['emailaddres']
        number=request.POST['number']
        message = request.POST['message']
        query="insert into contact(fullname,emailaddres,number,message) values('{0}','{1}','{2}','{3}')".format(fullname,emailaddres,number,message)
        print(query)
        cmd.execute(query)
        db.commit()
        db.close()
        return render(request,"contact.html",{'message':'Thank you for the Contacting us'})
    except Exception as e:
        print("Error:",e)
        return render(request,"login.html")


def booknow(request):
    try:
        db,cmd=pool.ConnectionPooling()
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        query="insert into book(name,email,number) values('{0}','{1}','{2}')".format(name,email,number)
        print(query)
        cmd.execute(query)
        db.commit()
        db.close()
        return render(request,"booknow.html",{'message':'Thank you for the Registration'})
    except Exception as e:
        print("Error:",e)
        return render(request,"login.html")