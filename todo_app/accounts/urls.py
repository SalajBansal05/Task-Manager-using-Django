from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('tasks/', views.task_all, name = 'task_all'),
    path('tasks/pending', views.task_pending, name = 'task_pending'),
    path('tasks/completed', views.task_completed, name = 'task_completed'),
    path('tasks/create/', views.task_create, name = 'task_create'),
    path('tasks/<int:id>/edit/', views.task_edit, name = 'task_edit'),
    path('tasks/<int:id>/toggle/', views.task_toggle, name = 'task_toggle'),
    path('tasks/<int:id>/delete/', views.task_delete, name = 'task_delete'),
]
