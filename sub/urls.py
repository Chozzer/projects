from django.urls import path
from sub import views
import sub




urlpatterns = [
    path("add_sub/<int:parent>", sub.views.add_sub, name='add_sub'),
    path("view_sub/<int:pk>", sub.views.view_sub, name = 'view_sub'),
    path("edit_sub/<int:pk>", sub.views.edit_sub, name = 'edit_sub'),
    path("delete_sub/<int:pk>", sub.views.delete_sub, name='delete_sub'),


]