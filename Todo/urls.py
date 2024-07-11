from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.todo, name='todo'),
    path('add_task/', views.add_task, name="add_task"),

    path('deleted_task/', views.deleted_task, name='deleted_task'),
    path('<int:task_id>/', views.delete_task, name='delete_task'),
]
