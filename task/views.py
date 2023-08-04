from django.shortcuts import render, redirect

from .models import Task

from .forms import NewTaskForm, UpdateTaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    return render(request, 'task/index.html', {'tasks': tasks})

def detail(request, pk):

    task = Task.objects.get(pk=pk)

    return render(request, 'task/detail.html', {'task':task})

def new(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form.save()
            # redirect after saving
            return redirect('/')
    else:
        form = NewTaskForm()

    return render(request, 'task/new.html', {'form': form})

def update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # redirect after saving
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)
    

    return render(request, 'task/update.html', {'task':task, 'form':form})

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect('/')
