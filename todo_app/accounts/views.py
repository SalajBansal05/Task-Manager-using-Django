from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username, password=password).exists():
            messages.error(request, 'User already exists.')
            return redirect('signup')
        
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        return redirect('login')
    
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'accounts/login.html')
        

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def task_all(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'accounts/task_list.html', {'tasks': tasks, 'page_title': 'All Tasks'})

@login_required
def task_pending(request):
    tasks = Task.objects.filter(user=request.user, completed=False)
    return render(request, 'accounts/task_list.html', {'tasks': tasks, 'page_title': 'Pending Tasks'})
    
@login_required
def task_completed(request):
    tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'accounts/task_list.html', {'tasks': tasks, 'page_title': 'Completed Tasks'})

@login_required
def task_create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        
        task = Task.objects.create(
            user = request.user,
            title = title, 
            description=description,
            deadline=deadline
        )
        task.save()
        return redirect('task_all')
    
    return render(request, 'accounts/task_create.html')

@login_required
def task_edit(request, id):
    task = Task.objects.get(id=id, user=request.user)
    if not task:
        messages.error(request, 'Task does not exist')
        return redirect('task_all')
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        if deadline:
            task.deadline = deadline
        task.save()
        return redirect('task_all')
    return render(request, 'accounts/task_create.html', {'task': task})

@login_required
def task_toggle(request, id):
    task = Task.objects.get(id=id, user=request.user)
    if not task:
        messages.error(request, 'Task does not exist')
        return redirect('task_all')
    
    if request.method == 'POST':
        if task.completed:
            task.completed = False
            task.completed_at = None
        else:
            task.completed = True
            task.completed_at = timezone.now()
        
        task.save()
        
    return redirect('task_all')

@login_required
def task_delete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    if not task:
        messages.error(request, 'Task does not exist')
        return redirect('task_all')
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_all')
    
    return render(request, 'accounts/task_delete.html', {'task': task})