from django.urls import path
from . import views

urlpatterns = [
    path('modules/', views.modules, name='modules'),
    path('exercise_detail/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
]