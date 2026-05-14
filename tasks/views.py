from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('tasks:tasks_list')
    return render(request, 'tasks/register.html', {'form': form})


@login_required
def tasks_list(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(owner=request.user)
    context = {
        'tasks': tasks,
        'total': tasks.count(),
        'pending': tasks.filter(status='pending').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'done': tasks.filter(status='done').count()
    }


    return render(request, 'tasks/tasks_list.html', context)

@login_required
def task_details(request, pk):
   
    task = get_object_or_404(Task, pk=pk)
    
    return render(request, 'tasks/task_details.html', {'task': task})



@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        messages.success(request, 'Task Created!')
        return redirect('tasks:tasks_list')
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, 'Task Updated!')
        return redirect('tasks:task_details', pk=pk)
    return render(request, 'tasks/task_form.html', {'form':form, 'action': 'Edit'})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task Deleted!')
        return redirect('tasks:tasks_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})





