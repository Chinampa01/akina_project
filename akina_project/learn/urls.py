from django.urls import path
from . import views

urlpatterns = [
    path('modules', views.modules, name='modules'),
]