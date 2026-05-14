from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('<int:pk>', views.task_details, name='task_details'),
    path('create/', views.create_task, name='create_task'),
    path('<int:pk>/edit', views.edit_task, name='edit_task'),
    path('<int:pk>/delete', views.delete_task, name='delete_task')
]