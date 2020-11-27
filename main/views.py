from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasts = Task.objects.all()
    print(tasts.values())
    return render(request, 'main/index.html', {'titlePage': 'Главная страница', 'pageContent' : 'Задачи', 'tasts': tasts})

def about(request):
    return render(request, 'main/about.html')

def addTask(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'main/addtask.html', {'form': TaskForm()})
