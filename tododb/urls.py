from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.ToDoList.as_view(), name='todo_list'),
    path('todo/<int:pk>', views.ToDoDetail.as_view(), name='todo_detail'),
]