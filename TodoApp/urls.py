from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('detail/<int:pk>/', views.TodoGetPost.as_view(), name='todo_detail'),
    path('create/', views.TodoGetPost.as_view(), name='todo_create'),
    path('done/<int:pk>/', views.TodoGetPost.as_view(), name='todo_done'),
    path('all/', views.TodoAllGet.as_view(), name='todo_all'),
]