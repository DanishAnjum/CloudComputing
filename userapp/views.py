from django.shortcuts import render,redirect

from .models import DataOwner,UploadFiles,DataUser
from cloudapp.models import UserRequest
from django.contrib import messages
import random
from django.db import connection
cursor = connection.cursor()
from django.conf import settings
from django.core.mail import send_mail
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# key = get_random_bytes(16)
import os

dataownerlogin='dologin.html'
dataownerreg = 'doreg.html'
dataownerhome = "dohome.html"
fileupload = "uploadfiles.html"
viewfile = "myfiles.html"
datauserlogin ="dulogin.html"
datauserreg = "dureg.html"
datuserhomepage ="duhome.html"
viewuserrequest = "userrequest.html"


# Create your views here.

# Data Owner Functions

def index(request):
    return render(request,'index.html')


def dologin(request):
    if request.method=="POST":
        Email=request.POST['email']
        password=request.POST['password']
        data= DataOwner.objects.filter(Email=Email,password=password).exists()
        print(data)
        if data ==True:

            request.session['doemail'] =Email
            n = random.randint(000000,999999)
            m1 = "This message is automatic generated so dont reply to this Mail"
            m2 = "Thanking you"
            m3 = "Regards"
            m4 = "Cloud."
            con = "use otp : {} to login ".format(str(n))
            Email =  Email
            subject = "REPOSITORY AND RETRIEVAL OF DATA USING CLOUD COMPUTING WITH AES SECURITY MEASURES"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Email]
            text =  m1 + '\n' + con + '\n' + m2 + '\n' + m3 + '\n' + m4
            send_mail(subject, text, email_from, recipient_list,fail_silently=False,)
            data= DataOwner.objects.get(Email=Email,password=password)
            data.OTP = str(n)
            data.save()
            return render(request,"otp.html")

            
        else:
            messages.warning(request,"Details doesn't exist's.")
            return render(request,dataownerlogin)
    return render(request,dataownerlogin)


def dootp(request):
    if request.method == "POST":
        Email = request.session['doemail']
        otp = request.POST['duotp']
        dc = DataOwner.objects.filter(Email=Email,OTP=otp).exists()
        if dc:
            return render(request,"dohome.html",{'email':Email})
        else:
            messages.warning(request,"Invalid Otp.")
            return redirect("dologin")

def doreg(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        password=request.POST['password1']
        conpasword=request.POST['password2']
        contact = request.POST['contact']
        address = request.POST['address']
        print(Name,Email,password,contact,address)
        if password == conpasword:
            data= DataOwner.objects.filter(Email=Email,password=password).exists()
            if data == False:
                data_insert =DataOwner(Name=Name,Email=Email,password=password,contact=contact,address=address)
                data_insert.save()
                return render(request,dataownerlogin)
            else:
                messages.warning(request,'Details already exists.')
                return render(request,dataownerreg)
        else:
            return render(request,dataownerreg)
    return render(request,dataownerreg)

def uploadfiles(request):
    global tag,nonce,ciphertext
    if request.method=="POST":
        uploaded_file = request.FILES['filedata']
        data = uploaded_file.read()
        print(uploaded_file)
        print(data)
        status = "pending"
        sql = "insert into userapp_uploadfiles(filename,filedata,encrypted_data,dataowner,status)values(%s,%s,AES_ENCRYPT(%s,'mykey'),%s,%s)"
        val = (uploaded_file.name,uploaded_file.name,data,request.session['doemail'],status)
        cursor.execute(sql,val)
        connection.commit()
        connection.close()
        


        
        return render(request,fileupload,{"msg":"file uploaded succesfully"})
    return render(request,fileupload)

def myfiles(request):
    data =UploadFiles.objects.filter(dataowner=request.session['doemail'])
    return render(request,viewfile,{"data":data})



# Data User Functions

def dulogin(request):
    if request.method=="POST":
        Email=request.POST['duemail']
        password=request.POST['password']

        data= DataUser.objects.filter(Email=Email,password=password).exists()
        print(data)
        if data ==True:
            request.session['Email'] = Email
            n = random.randint(000000,999999)
            m1 = "This message is automatic generated so dont reply to this Mail"
            m2 = "Thanking you"
            m3 = "Regards"
            m4 = "Cloud."
            con = "use otp : {} to login ".format(str(n))
            Email =  Email
            subject = "REPOSITORY AND RETRIEVAL OF DATA USING CLOUD COMPUTING WITH AES SECURITY MEASURES"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Email]
            text =  m1 + '\n' + con + '\n' + m2 + '\n' + m3 + '\n' + m4
            send_mail(subject, text, email_from, recipient_list,fail_silently=False,)
            data= DataUser.objects.get(Email=Email,password=password)
            data.OTP = str(n)
            data.save()
            return render(request,"otpuser.html")
        else:
            messages.warning(request,"Details doesn't exist's.")
            return render(request,datauserlogin)
    return render(request,datauserlogin)

def duotp(request):
    if request.method=="POST":
        Email = request.session['Email']
        otp = request.POST['otp']
        dc = DataUser.objects.filter(Email=Email,OTP=otp).exists()
        if dc:
            return render(request,"duhome.html",{'email':Email})
        else:
            messages.warning(request,"Invalid Otp.")
            return redirect("dulogin")


def dureg(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['duemail']
        password=request.POST['password1']
        conpasword=request.POST['password2']
        contact =request.POST['contact']
        address = request.POST['address']
        print(Name,Email,password,contact,address)
        if password == conpasword:
            data= DataUser.objects.filter(Email=Email,password=password).exists()
            if data == False:
                status='pending'
                data_insert =DataUser(Name=Name,Email=Email,password=password,contact=contact,address=address)
                data_insert.save()
                return render(request,datauserlogin)
            else:
                messages.warning(request,'Details already exists.')
                return render(request,datauserreg)
        else:
            return render(request,datauserreg)
    return render(request,datauserreg)


def viewdatausers(request):
    data =DataUser.objects.filter(last_name='pending')
    return render(request,'viewdatausers.html',{"datausers":data})


def acceptdatauser(request,id):
    data = DataUser.objects.get(id=id)
    # data.last_name='accepted'
    data.save()
    return redirect("viewdatausers")


def viewfiles(request):
    data = UploadFiles.objects.filter(status='pending')
    return render(request,'viewfiles.html',{'data':data})

def sendrequest(request,id):
    print(id)
    data = UploadFiles.objects.get(id=id)
    data.status='accepted'
    data.save()
    dataowner = data.dataowner
    filename = data.filename
    status = data.status
    encrypted_data = data.encrypted_data
    key = "tag"
    
    dc = UserRequest(fileid=id,Dataowner = dataowner,Datauser = request.session['Email'],Filename = filename ,status = status,encrypted_data=encrypted_data,key=key)
    dc.save()
    messages.add_message(request, messages.INFO, 'Request send to cloud')
    return redirect("viewfiles")



def viewresponse(request):
    dc = UserRequest.objects.filter(status='completed',Datauser=request.session['Email'])
    return render(request,'viewresponse.html',{'data':dc})

def viewdatafile(request,id):
    return render(request,"viewdatafile.html",{'id':id})


def mydatafile(request):
    if request.method=="POST":
        fid = request.POST['id']
        mykey = request.POST['key']
        print(fid,mykey)
        sql="select AES_DECRYPT(encrypted_data,'mykey') from userapp_uploadfiles where id=%s"%(fid)
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        if data !=[]:
            print(data)
            return render(request,'showfile.html',{'dc':data[0][0].decode()})
        else:
            messages.warning(request,'Enter the correct key')
            return render(request,'showfile.html')

def showfile(request,id):
    print(id)
    dc = UserRequest.objects.filter(id=id)
    print(dc)
    print(tag)
    dc  = [i.key for i in dc]
    print(dc)
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    print(data)

    return render(request,'showfile.html',{'dc':data})