from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="bug/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="bug/logout.html"),
        name="logout",
    ),
    path("addBug/", views.add, name="addBug"),
    path("del/<int:pk>", views.remove, name="del"),
]
