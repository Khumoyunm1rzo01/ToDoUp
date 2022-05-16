from datetime import date
from multiprocessing import context
from unicodedata import name
from django.shortcuts import redirect, render
from .models import*
# Create your views here.

def Home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        date = request.POST.get('date')
        ToDo.objects.create(task=task, date=date, status=False)
        return redirect('home')
    todo = ToDo.objects.all().order_by('-id')
    context = {
        'todo': todo,
    }
    return render(request, 'home.html', context)
def changestatus(request, pk):
    todo = ToDo.objects.get(id=pk)
    if todo.status:
        todo.status = False
        todo.save()
    else: 
        todo.status = True
        todo.save()  
    return redirect('home')

def passivetodos(request):
    todo = ToDo.objects.filter(status=True)
    context = {
        'todo': todo,
    }
    return render(request, 'passive.html', context)

def status(request):
    if request.method == "POST":
        status = request.POST.get('status')
        print(status)
        if status == '2':
            return redirect('passive-todos')
        elif status == '3':
            return redirect('active')
        elif status == '1':
            return redirect('home')
    return redirect('home')

def deletetodo(request, pk):
    todo = ToDo.objects.get(id=pk)
    DeletedTodo.objects.create(task=todo.task, date=todo.date, status=todo.status)
    todo.delete()
    return redirect('home')

def activetodos(request):
    todo = ToDo.objects.filter(status=False)
    context = {
        'todo': todo,
    }
    return render(request, 'active.html', context)

def changetask(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        todo = ToDo.objects.get(id=id)
        todo.task = name
        todo.date = date
        todo.save()
        return redirect('home')
    return redirect('home')