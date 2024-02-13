from django.urls import path
from . import views

# Urls for REST API
urlpatterns = [
    path('todoTask/<int:pk>', views.TodoTaskView.as_view()),
    path('todoTask/', views.TodoTaskView.as_view(),name="All To Do Tasks"),
]