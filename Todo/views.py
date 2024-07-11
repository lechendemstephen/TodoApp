from django.shortcuts import render # type: ignore
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo(request): 
    task = Todo.objects.all()


    context = {
        'tasks': task
    }

    return render(request, 'Todo/pages/todo.html', context)

def add_task(request): 
    if request.method == "POST": 
        form = TodoForm(request.POST)
        if form.is_valid():
           data = Todo()
           data.title = form.cleaned_data['title']
           data.task = form.cleaned_data['task']
           data.dead_line = form.cleaned_data['dead_line']
           data.save()
           print('saved successfully')

    else: 
        form = TodoForm


    return render(request, 'Todo/pages/add_task.html')