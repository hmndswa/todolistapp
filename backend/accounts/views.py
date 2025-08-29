from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()     # creates the user in PostgreSQL (auth_user)
            login(request, user)   # auto-login after signup
            return redirect('tdlapp:list_todos')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
