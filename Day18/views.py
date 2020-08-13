from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import *


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    data = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    print(tasks)
    return render(request, 'tasks/list.html', data)


def editTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/edit.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
