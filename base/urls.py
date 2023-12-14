from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    #path("login/", views.login_user, name="login" ),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name = "register"),
    path("project/<int:pk>", views.project_view, name = "project_view"),
    path("add_subproject", views.add_subproject, name="add_subproject")



]