from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Department Admin'),
        ('user', 'Citizen'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)