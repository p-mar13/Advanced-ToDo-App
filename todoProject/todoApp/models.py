from django.db import models

# Create your models here.

class ToDoTask(models.Model):
    task=models.CharField(max_length=80)
    status=models.CharField(max_length=10)
    description=models.CharField(max_length=200)


