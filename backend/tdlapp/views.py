from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            Todo.objects.create(user=request.user, title=title)
        return redirect('tdlapp:list_todos')
    return render(request, 'todo/addtdl.html')

@login_required
def list_todos(request):
    todos = (Todo.objects
                  .filter(user=request.user, completed=False)
                  .order_by('-created_at'))
    return render(request, 'todo/listtdl.html', {'todos': todos})

@login_required
def edit_todo(request, pk):
    t = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            t.title = title
            t.save()
            return redirect('tdlapp:list_todos')
        return render(request, 'todo/edittdl.html', {'todo': t, 'error': 'Title cannot be empty.'})
    return render(request, 'todo/edittdl.html', {'todo': t})

@login_required
def delete_todo(request, pk):
    t = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        t.delete()
        return redirect('tdlapp:list_todos')
    return render(request, 'todo/deletetdl.html', {'todo': t})

@login_required
def toggle_todo(request, pk):
    if request.method == 'POST':
        t = get_object_or_404(Todo, pk=pk, user=request.user)
        t.completed = not t.completed
        t.save()
    return redirect('tdlapp:list_todos')
