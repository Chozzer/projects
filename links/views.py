from django.shortcuts import render, redirect
from  base.models import link, status, project

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
    
def delete_link(request, link_id):
    link.objects.filter(id=link_id).delete
    return redirect('home')