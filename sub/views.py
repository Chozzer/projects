from django.shortcuts import render, redirect
from base.models import project, status, type,  note, task, link
from django.utils import timezone

# Create your views here.



def view_sub(request, pk):
    if request.user.is_authenticated:
        subproject = project.objects.get(pk=pk)
        notes = note.objects.filter(ref=pk)
        tasks = task.objects.filter(ref=pk)
        links = link.objects.filter(ref=pk)
        return render(request, 'view_subproject.html', {'sub': subproject, 'notes':notes, 'tasks':tasks, 'links':links })
    else:
        return redirect('home')




def add_sub(request, parent):
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
            newproject = project.objects.create( parent = parent, 
                                                name = name,  
                                                description = description,  
                                                completed = completed, 
                                                archived = archived, 
                                                lastActivity = lastActivity, 
                                                type_id = result.id, 
                                                status_id=pstatus.id)
            newproject.save
            return redirect('home')
        else:
            types = type.objects.all()
            pstatus = status.objects.all()
            return render(request, 'add_subproject.html' , {'parent':parent, 'types':types, 'status': pstatus})
    else:
        return redirect('home')



def edit_sub(request, pk):
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
            sub_to_edit = project.objects.get(pk= pk)
            pstatus= status.objects.all()
            ptype = type.objects.all()
            return render(request, "edit_subproject.html", {"sub":sub_to_edit, "status":pstatus, "type":ptype })
        
        
        return redirect('home')
    else:
        return redirect('home')

def delete_sub(request, pk):
    project.objects.get(id=pk).delete()
    return redirect('home')




