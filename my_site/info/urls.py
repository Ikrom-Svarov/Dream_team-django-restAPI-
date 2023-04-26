from django.urls import path

from .views import IndexView,  DeleteTaskView, TaskDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:task_pk>/delete', DeleteTaskView.as_view(), name='delete'),
    path('<int:task_id>/', TaskDetailView.as_view(), name='view'),
]