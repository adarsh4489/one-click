from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def registration(request):
    try:
        db,cmd=pool.ConnectionPooling()
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        phoneno=request.POST['phoneno']
        query="insert into registration(name,username,email,password,phoneno) values('{0}','{1}','{2}','{3}','{4}')".format(name,username,email,password,phoneno)
        print(query)
        cmd.execute(query)
        db.commit()
        db.close()
        return render(request,"login.html",{'message':'Thank you for the Registration'})
    except Exception as e:
        print("Error:",e)
        return render(request,"register.html",{'message':'Something went wrong'})

def Login(request):
    return render(request,'login.html',{'msg':''})

def CheckLogin(request):
    try:
        db,cmd=pool.ConnectionPooling()
        email=request.POST['email']
        password=request.POST['password']
        q = "select * from registration where email='{0}' and password='{1}'".format(email,password)
        cmd.execute(q)
        record = cmd.fetchone()
        if(record):
         request.session['user']=record
         return render(request, 'index.html', {'message':'','data':record})
        else:
         return render(request, 'login.html', {'message': "Invalid EmailId/Password"})
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'message': 'Server Error'})
