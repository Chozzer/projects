from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.db.models import Max
from .forms import SignUpForm
from .models import project, status, note, task, link, type




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


def create_project(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            ptype = request.POST["type"] 
            result = type.objects.get(type=ptype)
            pstatus = request.POST["status"]
            pstatus=status.objects.get(status=pstatus)
            description = request.POST["description"]
            completed = False
            archived = False
            lastActivity = timezone.now()
            newproject = project.objects.create( parent = 0, 
                                                name = name,  
                                                description = description,  
                                                completed = completed, 
                                                archived = archived, 
                                                lastActivity = lastActivity, 
                                                type_id = result.id, 
                                                status_id=pstatus.id)
            #newproject = project( parent = parent, name = name, type = 1, description = description, status = status, completed = completed, archived = archived, lastActivity = lastActivity)
            newproject.save
            return redirect('home')



        else:
            types = type.objects.all()
            pstatus = status.objects.all()
            return render(request, 'createproject.html' , {'types':types, 'status': pstatus})
    
    else:
            return redirect('home')
    
def edit_project(request, pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            posted_status = request.POST["status"]
            newstatus=status.objects.get(status=posted_status)
            posted_type = request.POST["type"]
            newtype = type.objects.get(type = posted_type)
            subproject = project.objects.get(id=pk)
            subproject.name = request.POST["name"]
            subproject.description = request.POST["description"]
            subproject.type_id = newtype.id
            subproject.status_id = newstatus.id
            subproject.save
        else:
            project_to_edit = project.objects.get(pk= pk)
            pstatus= status.objects.all()
            ptype = type.objects.all()
            return render(request, "edit_project.html", {"project":project_to_edit, "status":pstatus, "type":ptype })

    else:
        return redirect('home')





    




    





def add_link(request, parent):
    if request.user.is_authenticated:
        if request.method=="POST":
            pkref= project.objects.get(pk=parent)
            title=request.POST["title"]
            url=request.POST["link"]
            newlink = link.objects.create(ref_id=pkref.id,
                                            title=title,
                                            url=url,
                                            )
            newlink.save
            return redirect('home')
                
        else:
            return render(request, 'add_link.html', {})
    else:
        return redirect('home')
    

    
def add_note(request, parent):
    if request.user.is_authenticated:
        if request.method=="POST":
            pkref= project.objects.get(pk=parent)
            title=request.POST["title"]
            text=request.POST["text"]
            newnote = note.objects.create(ref_id=pkref.id,
                                            title=title,
                                            text=text,
                                            )
            newnote.save
            return redirect('home')
                
        else:
            return render(request, 'add_note.html', {})
    
    else:
        return redirect('home')
    

def add_type(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            posted_type = request.POST["type"]
            newtype = type.objects.create(type=posted_type)
            newtype.save
        else:
            types  = type.objects.all()
            return render(request, "add_type.html", {'types':types})
    return redirect('home')
    

def add_status(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            posted_status = request.POST["status"]
            newstatus = status.objects.create(status=posted_status)
            newstatus.save
            
        else:
            statuses  = status.objects.all()
            return render(request, "add_status.html", {'statuses':statuses})

    return redirect('home')