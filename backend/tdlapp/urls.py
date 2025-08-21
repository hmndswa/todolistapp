from django.urls import path
from . import views

app_name = 'tdlapp'

urlpatterns = [
    path('', views.list_todos, name='list_todos'),
    path('add/', views.add_todo, name='add_todo'),
]