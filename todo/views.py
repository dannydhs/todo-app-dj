from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todo/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect("todo:task_list")
    return render(request, 'todo/add_task.html')


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('todo:task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        task.title = request.POST['title']
        task.save()
        return redirect('todo:task_list')
    
    return render(request, "todo/edit_task.html", {"task": task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('todo:task_list')
