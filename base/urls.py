from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    
    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),
    path('room-create', views.createRoom, name='create-room'),
    path('room-update/<str:pk>', views.updateRoom, name='update-room'),
    path('room-delete/<str:pk>', views.deleteRoom, name='delete-room')
]