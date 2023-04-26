"""
URL configuration for dream_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from info.views import  TaskCreateView, TaskUpdateView, RegistrationView,AuthLoginView, logout_view, TaskView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('info.urls')),
    path('task/',TaskView.as_view(), name='task' ),

    path('create/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('registеr/', RegistrationView.as_view(), name='register'),
    path('login/', AuthLoginView.as_view(), name='login' ),
    path('logout/', logout_view, name='logout'),


    

]