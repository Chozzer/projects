from django.shortcuts import render, redirect
from base.models import project, status, type, note


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


def edit_note(request, req_note):
    if request.user.is_authenticated:
        if request.method=='POST':
            pstatus = request.POST["status"]
            pstatus=status.objects.get(status=pstatus)
            note_to_edit = note.objects.get(pk=req_note)
            note_to_edit.id = request.post['id']
            note_to_edit.title
            note_to_edit.text
        else:
            pstatus= status.objects.all()
            note_to_edit = note.objects.get(pk=req_note)
            return render(request, 'edit_note.html',{'status':pstatus, 'note':note_to_edit})

    else:
        return redirect('home')
        

def display_note(request, req_note):
    if request.user.is_authenticated:
        note_to_display = note.objects.get(pk = req_note)
        return render(request, 'display_note.html',{'note':note_to_display})
    else:
        return redirect("home")


def delete_note(request, req_note):
    note.objects.filter(id=req_note).delete()
    return redirect('home')