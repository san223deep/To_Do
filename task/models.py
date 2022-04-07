from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Task(models.Model):
    STATES = (
        ('T', 'TODO'),
        ('P', 'in Progress'),
        ('D', 'Done')
    )
    user = models.ForeignKey('task.User', on_delete=models.CASCADE, related_name='tasks')
    state = models.CharField(max_length=1, choices=STATES, default='T')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

