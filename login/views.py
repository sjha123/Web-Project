from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        ms = sql.connect(host='localhost',user='root',passwd='Shubham1@',database='website')
        cur= ms.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cur.execute(c)
        t=tuple(cur.fetchall())
        fname = t[0][0]
        lname = t[0][1]
        if t==():
            return render(request,'error.html')
        else:
            messages.success(request, "You have logged in succesfully!!")
            return render(request,'welcome.html',{"fname":fname,"lname":lname})
       

    return render(request,'login_page.html')