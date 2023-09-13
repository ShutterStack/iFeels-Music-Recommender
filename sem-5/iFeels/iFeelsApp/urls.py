from django.contrib import admin
from django.urls import path
from iFeelsApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("forgot", views.forgot, name='forgot'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("camera", views.camera, name='camera'),
    path("login", views.login, name='login'),




    ]
