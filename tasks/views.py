from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks=Task.objects.all()    
    else:
        tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/list.html', {'tasks': tasks, 'form':form})

@login_required
def task_create(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=request.user
            task.save()
        return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html')

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return redirect('task_list')
