from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout



def home(request):
	return render(request , 'index.html')

@login_required(login_url='login')
def todolist(request):
	tasks = Task.objects.all()
	context = {'tasks':tasks}
	return render(request , 'todo/register.html' , context)

@login_required(login_url='login')
def createTask(request):
	form  = TaskForm
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todolist')
	context = {'form':form}
	return render(request,'todo/task_form.html',context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exist')
		
		user = authenticate(request,username=username,email=email,password=password)
		
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.error(request,'Username or password incorrect')

	context = {}
	return render(request, 'todo/login.html' ,context)

def logoutPage(request):
	logout(request)
	return redirect('home')
