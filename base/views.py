from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .forms import SignUpForm
from .models import project, note, task, link



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
        subprojects = project.objects.filter(parent=pk)
        notes = note.objects.filter(ref=pk)
        tasks = task.objects.filter(ref=pk)
        links = link.objects.filter(ref=pk)
        return render(request, 'project_view.html', {'project': result, 'notes':notes, 'tasks':tasks, 'links':links, 'subprojects': subprojects  })
    else:
        return redirect('home')

    
def add_subproject(request, parent):
     if request.method == "POST":
        parent = request.POST["parent"]
        name = request.POST["name"]
        type = request.POST["type"] 
        description = request.POST["description"]
        status = request.POST["status"]
        completed = False
        archived = False
        lastActivity = timezone.now()
          
          
     else:
        return render(request, 'add_subproject.html' , {'parent':parent})
