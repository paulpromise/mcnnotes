from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Note paths
    path('', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    
    # Subject paths
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
    path('subjects/<int:pk>/', views.subject_detail, name='subject_detail'),
]
