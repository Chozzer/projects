from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import project


# Create your views here.

#home page. 
# if not logged in, will display login
# if request = post will process login
# else will list all current projects




def home(request):
    projects = project.objects.filter(parent=0)
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
        return render(request, 'home.html', {'projects': projects})
#def login_user(request):
    


def logout_user(request):
    logout(request)
    return redirect("home")
    

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def project_view(request, pk):
    if request.user.is_authenticated:
        result = project.objects.get(id=pk)
        return render(request, 'project_view.html', {'project': result})
    

    else:
         return redirect('home')

    
