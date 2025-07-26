from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
import logging

# Create your views here.

@csrf_exempt
def  register(request):
    if(request.method == 'GET'):
        return HttpResponse("Welcome to accounts Homepage")
    if(request.method == 'POST'):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            new_user = User.objects.create_user(username=username,email=email, password=password)
            group_object = Group.objects.get(name = 'Reader')
            new_user.groups.add(group_object)
            print(new_user.groups.name)
            return HttpResponse("Success... Welcome Onboard")
        except:
            print("Error at backend....")

@csrf_exempt
def login_user(request):
    if(request.method == 'GET'):
        return HttpResponse('Please enter details to login')
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
    user_active = authenticate(username = username,password = password)
    if(user_active ==  None):
        return HttpResponse("No User Found with such credentials")
    else:
        login(request=request,user = user_active)
        return HttpResponse("Success.. Welcome " + request.user.username +"...")
    
@csrf_exempt
def logout_user(request):
    if(request.user.is_authenticated):
        print(request.user)
        logout(request)
        print(request.user)
        return HttpResponse("Logout Succesful")
    else:
        return HttpResponse("No user Logged In")
    


