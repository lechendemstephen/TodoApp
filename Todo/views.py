from django.shortcuts import render, redirect# type: ignore
from .models import Todo
from .forms import TodoForm
from django.contrib import messages # type: ignore
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # type: ignore
# Create your views here.

def todo(request): 
    task = Todo.objects.all()

    # pagination for the task 
    p = Paginator(task, 6) # first argument is the list of objects that will be dispayed
    # getting the desired page from the url 
    page_number = request.GET.get('page')

    try: 
        page_obj = p.get_page(page_number) # return desired page objects 
    
    except PageNotAnInteger: 
        page_obj = p.page(1)
    except EmptyPage: 
        page_obj = p.page(p.num_pages)


    context = {
        'tasks': task,
        'page_obj': page_obj
    }

    return render(request, 'Todo/pages/todo.html', context)

# Adding 
def add_task(request): 
    if request.method == "POST": 
        form = TodoForm(request.POST)
        if form.is_valid():
           data = Todo()
           data.title = form.cleaned_data['title']
           data.task = form.cleaned_data['task']
           data.dead_line = form.cleaned_data['dead_line']
           data.save()
           messages.success(request, 'Task Successfully Added')

           return redirect('add_task')

    else: 
        form = TodoForm

    return render(request, 'Todo/pages/add_task.html')


# deleting task
def deleted_task(request): 

    return render(request, 'Todo/pages/deleted_task.html')


def delete_task(request, task_id): 
    task = Todo.objects.filter(id=task_id)
    task.delete()
    messages.success(request, 'Task Deleted')
    return redirect('todo')

    return render(request, 'Todo/pages/todo.html')