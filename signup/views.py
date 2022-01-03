from django.shortcuts import render
import mysql.connector as sql
# fn=''
# ln=''
# s=''
em=''
nm=''
mn=''
ct=''
rf=''
pwd=''
# Create your views here.
def signaction(request):
    global em,nm,mn,ct,rf,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Rbic#123",database='sys')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="name":
                nm=value
            if key=="mobile_number":
                mn=value
            if key=="city":
                ct=value  
            if key=="referral_code":
                rf=value           
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(em,nm,mn,ct,rf,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')