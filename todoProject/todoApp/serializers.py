from rest_framework import serializers
from .models import ToDoTask

# Serializers for all models

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'
