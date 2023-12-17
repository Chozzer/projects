from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    #path("login/", views.login_user, name="login" ),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name = "register"),
    path("project/<int:pk>", views.project_view, name = "project_view"),
    path("add_subproject/<int:parent>", views.add_subproject, name="add_subproject"),
    path("add_task/<int:parent>", views.add_task, name='add_task'),
    path("add_link/<int:parent>", views.add_link, name="add_link"),
    path("add_note/<int:parent>", views.add_note, name="add_note"),
    path("create_project/", views.create_project, name="create_project")



]