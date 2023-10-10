from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):

    return render(request,"home.html")

def first(request):

    return render(request,'third.html')

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account-type']
        materials = request.POST['materials']

        return HttpResponse(f'<center><p>Application Accepted</p><p><a href="/">Return to Home Page</a></p></center>')


    return render(request,'form.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(
            username=username,password=password
        )
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                username=username,
                password=password
                )
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')