from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def add_todo(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            Todo.objects.create(title=title)
        return redirect('tdlapp:list_todos') 
    return render(request, 'todo/addtdl.html') 

def list_todos(request):
    todos = Todo.objects.filter(completed=False).order_by('-created_at')
    return render(request, 'todo/listtdl.html', {'todos': todos})


def delete_todo(request, pk):
    t = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        t.delete()
        return redirect('tdlapp:list_todos')
    return render(request, 'todo/deletetdl.html', {'todo': t})

def edit_todo(request, pk):

    t = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            t.title = title
            t.save()
            return redirect('tdlapp:list_todos')
        return render(request, 'todo/edittdl.html', {'todo': t, 'error': 'Title cannot be empty.'})
    
    return render(request, 'todo/edittdl.html', {'todo': t})

def toggle_todo(request, pk):
    if request.method == 'POST':
        t = get_object_or_404(Todo, pk=pk)
        t.completed = not t.completed
        t.save()
    return redirect('tdlapp:list_todos')