from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#home page. 
# if not logged in, will display login
# if request = post will process login
# else will list all current projects




def home(request):
    return render(request, "home.html")

#def login_user(request):
    


def logout_user(request):
    pass


