from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#home page. 
# if not logged in, will display login
# if request = post will process login
# else will list all current projects
# maybe the projects model will have a status, with one being not very important and three being really important. This will link to a seperate status model



def home(request):
    return render(request, "home.html")

def login_user(request):
    pass


def logout_user(request):
    pass


