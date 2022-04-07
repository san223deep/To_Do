from django.urls import path
from . import views
from rest_framework.authtoken import views as token_view

urlpatterns = [
    path('todo_list/', views.ToDoList.as_view()),
    path('todo_list/<pk>/', views.ToDoListUpdate.as_view()),
    path('get-api-token/', token_view.obtain_auth_token)
]
