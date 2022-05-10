from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

fn=''
ln=''
gen=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,gen,em,pwd
    if request.method=="POST":
        ms = sql.connect(host='localhost',user='root',passwd='@',database='website')
        cur= ms.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                gen=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        usr="select * from users where email='{}'".format(em)
        cur.execute(usr)
        t=tuple(cur.fetchall())
        if t==():
            c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,gen,em,pwd)
            cur.execute(c)
            ms.commit()
            messages.success(request, 'Registration completed successfully!!')
        
        else:
            messages.error(request, ' Email ID already exist!!')
            #return render(request,'error.html')

    return render(request,'signup_page.html')
