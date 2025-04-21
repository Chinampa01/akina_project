from django.db import models

class Module(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    order = models.PositiveIntegerField(blank=False, null=False)    

class Exercise(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    LEVEL_CHOICES = [('B', 'Básico'), ('I', 'Intermedio'), ('A', 'Avanzado')]
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, blank=False, null=False)
    instruction = models.TextField(blank=False, null=False)
    starter_code = models.TextField(blank=True)