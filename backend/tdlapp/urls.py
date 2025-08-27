from django.urls import path
from . import views

app_name = 'tdlapp'

urlpatterns = [
    path('', views.list_todos, name='list_todos'),
    path('add/', views.add_todo, name='add_todo'),
    path('todo/<int:pk>/edit/', views.edit_todo, name='edit_todo'),
    path('todo/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
    path('todo/<int:pk>/toggle/', views.toggle_todo, name='toggle_todo'),
]