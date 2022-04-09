from rest_framework import serializers
from .models import Task
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'state', 'due_date')


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')

    def validate(self, attrs):
        due_date = attrs['due_date']
        today = date.today()
        if due_date < today:
            raise serializers.ValidationError('Due date must be a future date')
        return attrs


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'state')
