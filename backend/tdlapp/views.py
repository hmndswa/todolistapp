from django.shortcuts import render, redirect
from .models import Todo

def add_todo(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            Todo.objects.create(title=title)
        return redirect('tdlapp:list_todos') 
    return render(request, 'todo/addtdl.html') 

def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/listtdl.html', {'todos': todos})
