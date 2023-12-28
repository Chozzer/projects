from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.db.models import Max
from base.forms import SignUpForm
from base.models import project, status, note, task, link, type

# Create your views here.
def add_task(request, parent):
    if request.user.is_authenticated:
        if request.method == "POST":
            pkref= project.objects.get(pk=parent)
            ref = pkref.name
            title = request.POST["title"]
            new_task = request.POST["task"]
            pstatus = request.POST["status"]
            pstatus=status.objects.get(status=pstatus)
            next_order = task.objects.aggregate(Max('order')).get('order__max')
            next_order = next_order +1
            newtask = task.objects.create(ref_id=pkref.id,
                                        title=title,
                                        task=new_task,
                                        order=next_order,
                                        status_id=pstatus.id)
            newtask.save
            projectid=parent
            return redirect('home')
            
        else:
            pstatus= status.objects.all()
            return render(request, 'add_task.html', {'status':pstatus})
    else:
        print("not logged in")
        return redirect('home')
    


def display_task(request, req_task):
    if request.user.is_authenticated:
        task_to_display = task.objects.get(pk=req_task)
        return render(request, 'display_task.html', {'task':task_to_display})
    
    else:
        return redirect('home')
    
def edit_task(request, req_task):
    if request.user.is_authenticated:
        if request.method=="POST":
            id = req_task
            pstatus = request.POST["status"]
            pstatus=status.objects.get(status=pstatus)
            edited = task.objects.get(id=id)
            edited.title = request.POST["title"]
            edited.task = request.POST["task"]
            edited.order = request.POST["order"]
            edited.status_id = pstatus.id
            edited.save()
            return redirect("home")

        else:
            task_to_edit = task.objects.get(pk=req_task)
            pstatus= status.objects.all()
            return render(request, 'edit_task.html', {'task':task_to_edit, 'status':pstatus})
    
    else:
        return redirect('home')


def delete_task(request, req_task):
    task.objects.filter(id=req_task).delete()
    return redirect('home')