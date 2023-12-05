from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#home page. 
# if not logged in, will display login
# if request = post will process login
# else will list all current projects




def home(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.success(request, "There was a problem")
            return redirect("home")
    else:
        return render(request, 'home.html')
#def login_user(request):
    


def logout_user(request):
    logout(request)
    return redirect("home")
    


