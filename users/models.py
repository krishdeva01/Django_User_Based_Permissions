from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)

    # Add unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",  # Unique related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  # Unique related_name
        related_query_name="user",
    )

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey('User', on_delete=models.CASCADE, related_name='assigned_tasks_to')
    assigned_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='assigned_tasks_by')
    completed = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title