from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name = "register"),
    path("project/<int:pk>", views.project_view, name = "project_view"),
    path("edit_project/<int:pk>", views.edit_project, name="edit_project"),
    #path("add_note/<int:parent>", views.add_note, name="add_note"),
    path("create_project/", views.create_project, name="create_project"),
    path("add_type", views.add_type, name="add_type"),
    path("add_status", views.add_status, name="add_status")

]