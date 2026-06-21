from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class registration_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnic = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
