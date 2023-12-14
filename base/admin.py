from django.contrib import admin
from .models import project, type, status, note, task, link


# Register your models here.
admin.site.register(project)
admin.site.register(type)
admin.site.register(status)
admin.site.register(note)
admin.site.register(task)
admin.site.register(link)