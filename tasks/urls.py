from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_tasks, name = 'list_of_tasks'),
    path('add/', views.add_new_task, name = 'add_new_task'),
]