from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import category
from.form import AddForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth

# Create your views here.


def say_hello(request):
    # return HttpResponse('hello world')
    return render(request,'hello.html',{'name':'Mosh'})

def index(request):
    return render(request,'index.html')

def loginn(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

#to database

def insert(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        gender=request.POST.get('gender')
        category(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,password=password,confirmpassword=confirmpassword,gender=gender).save()
    return render(request,"signup.html")

def view(request):
    cr= category.objects.all()
    return render(request,"view.html",{'cm':cr})

#for detailed view

def detailed_view(request,pk):
    cr = category.objects.get(id=pk)
    return render(request,'detailedview.html',{'cm':cr})

#delete

def delete(request,pk):
    cr = category.objects.get(id=pk)
    cr.delete()
    return redirect("view")

#update

def update(request,pk):
    cr=category.objects.get(id=pk)
    form=AddForm(instance=cr)
    if request.method=="POST":
        form=AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("view")
    return render(request,"update.html",{'form':form})

def loginform(request):
   if request.method=="GET":
        return render(request,"login.html")

#login

def userlog(request):
    if request.method=='POST':
        #saving the entered data into a new variable
        firstnamefromUI = request.POST.get('firstname')
        passwordfromUI = request.POST.get('password')
        
        #filtering the database[data] such that anyone who is having the combination of this username and password are stored in cr variable
        cr = category.objects.filter(firstname=firstnamefromUI,password=passwordfromUI)
        
        if cr:
            #get a single data which matches the condition passed into it
            user_details=category.objects.get(firstname=firstnamefromUI,password=passwordfromUI)
            
            
            id=user_details.id
            firstname=user_details.firstname
            email=user_details.email
            

            request.session['id']=id
            request.session['firstname']=firstname
            request.session['email']=email
    

          

    
          

            return redirect('welcome')
        else:
            #return redirect('login')
             return render(request,'login.html',{'message':"entered wrong credentials"})
    else:
        return render(request,'view.html')
        


def welcome(request):
   id=request.session['id']
   email=request.session['email']
   return render(request,"welcome.html",{'id':id,'email':email})


#logout

def logoutuser(request):
    logout(request)
    return redirect('login')

#admin

def adminlog(request):
     return render(request,"adminlog.html")

#make admin

def alog(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        password = request.POST['password']
        user=auth.authenticate(firstname=firstname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('adminlog')
    else:
        return render(request,'adminlog.html')
   



