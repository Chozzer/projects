from django.contrib import admin
from .models import project, type, status

# Register your models here.
admin.site.register(project)
admin.site.register(type)
admin.site.register(status)