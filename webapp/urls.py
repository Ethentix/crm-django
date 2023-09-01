from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=""),
    path('register/', views.register, name="register"),
    path('login/', views.user_Login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard" ),
    path('userLogout/', views.user_LogOut, name="userLogout"),
    path('add-record/', views.create_record, name="add-record"),
    path('update-record/<int:pk>/', views.update_record, name="update-record"),
    path('record/<int:pk>/', views.single_record, name="record"),
    path('delete-record/<int:pk>/', views.delete_record, name="delete-record"),
]

