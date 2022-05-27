from django.urls import path
from .views import *

urlpatterns = [
	path('', apiOverview),
    path('task-list/', taskList),
    path('task-detail/<str:pk>/', taskDetail),
    path('task-create/', taskCreate),
    path('task-update/<str:pk>/', taskUpdate),
    path('task-delete/<str:pk>/', taskDelete),
]