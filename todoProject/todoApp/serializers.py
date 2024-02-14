from rest_framework import serializers
from .models import ToDoTask, Category, TaskStatus

# Serializers for all models

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
        


class ToDoSerializer(serializers.ModelSerializer):
    status=StatusSerializer()
    category=CategorySerializer()
    class Meta:
        model = ToDoTask
        fields='__all__'
        
