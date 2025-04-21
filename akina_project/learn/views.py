from django.shortcuts import render
from .models import Module

def modules(request):
    modules = Module.objects.all().order_by('order')
    return render(request, 'learn/modules.html', {'modules': modules})