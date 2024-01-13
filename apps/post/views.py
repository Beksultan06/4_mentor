from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


@login_required
def task_list(request):
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'all':
        tasks = Task.objects.filter(user=request.user)
    else:
        status_value = True if status_filter == 'completed' else False
        tasks = Task.objects.filter(user=request.user, status=status_value)

    tasks = tasks.order_by('due_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks, 10)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    return render(request, 'task/task_list.html', {'tasks': tasks, 'status_filter': status_filter})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})


@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/task_detail.html', {'task': task})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'register/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')