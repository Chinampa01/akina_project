from django.shortcuts import render
from .models import Module, Exercise
from django.http import HttpResponse

def modules(request):
    modules = Module.objects.all().order_by('order')
    return render(request, 'learn/modules.html', {'modules': modules})

def exercise_detail(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    return render(request,'learn/exercise_detail.html', {'exercise': exercise})