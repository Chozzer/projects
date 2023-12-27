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
            return redirect('home')
            
        else:
            pstatus= status.objects.all()
            return render(request, 'add_task.html', {'status':pstatus})
    else:
        return redirect('home')