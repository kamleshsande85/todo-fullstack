from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<int:pk>/', views.getTask),
    path('tasks/<int:pk>/delete/', views.deleteTask),
    path('tasks/<int:pk>/update/', views.updateTask),

]
