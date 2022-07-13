from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
#add the models library to fetch data and display it
from todolist.models import TaskList
#import forms for DB
from todolist.form import TaskForm
#display messages
from django.contrib import messages
#import pagination
from django.core.paginator import Paginator
#decorator function for login permission
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,("New Task Added!!!"))
        return redirect('todolist')

    else:
        # fetch all data from model
        all_tasks= TaskList.objects.filter(manage=request.user)
        #pagination
        paginator=Paginator(all_tasks,5)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)

        return render(request,'todolist.html',{'all_tasks':all_tasks})
@login_required
def delete_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted!!!"))
    return redirect('todolist')
@login_required
def edit_task(request,task_id):
     if request.method == "POST":
        task= TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')

     else:
        # fetch all data from model
        task_obj= TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
@login_required
def complete_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricted!!!"))
    return redirect('todolist')
@login_required
def pending_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    task.done =False
    task.save()
    return redirect('todolist')

def index(request):
    
    context={'index_text':"Welcome to the Index Page",
    }
    return render(request,'index.html',context)


def contact(request):
    context={'contact_text':"Welcome to the Contact Page",
    }
    return render(request,'contact.html',context)

def about(request):
    
    context={'about_text':"Welcome to the About Page",
    }
    return render(request,'about.html',context)

