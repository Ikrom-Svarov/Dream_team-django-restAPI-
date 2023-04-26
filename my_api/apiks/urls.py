from django.urls import path

from .views import TaskApiList, TaskApiRetrieve, TaskApiCreate

urlpatterns = [
    path('list/', TaskApiList.as_view()),
    path('create/', TaskApiCreate.as_view()),
    path('<int:pk>/', TaskApiRetrieve.as_view()),
]