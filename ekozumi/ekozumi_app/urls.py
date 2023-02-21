from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Url patterns for the ekozumi application
urlpatterns = [
    path("register/", views.registrationPage, name="ekozumi-register"),
    path("", auth_views.LoginView.as_view(template_name='ekozumi_app/login.html'), name="login"),
    path("home/", views.homePage, name="home_page"),
    path("zumi_creation/", views.zumiCreationPage, name="zumi_creation"),
]