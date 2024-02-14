from typing import Any
from django.db import models

# Create your models here.

class TaskStatus(models.Model):
    current_status=models.CharField(max_length=12)
    closed=models.BooleanField()
    def __str__(self) -> str:
        return self.current_status


class ToDoList(models.Model):
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.date
    
class Category(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField()
    description=models.CharField()


class ToDoTask(models.Model):
    task=models.CharField(max_length=80)
    status=models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    created_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    def __str__(self):
        return self.task
    






