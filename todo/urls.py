from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("",views.home, name='home'),
    path("login/",views.loginPage, name='login'),
    path("logout/",views.logoutPage, name='logout'),
    path("todolist/",views.todolist, name='todolist'),
    path("create-task/",views.createTask, name='create-task'),

    


]
