from django.db import models

# Create your models here.

class ToDoList(models.Model):
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.date

class ToDoTask(models.Model):
    task=models.CharField(max_length=80)
    status=models.CharField(max_length=12)
    description=models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    #todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    def __str__(self):
        return self.task




