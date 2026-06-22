
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# department from account
from accounts.models import Department
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    description = models.TextField()
    evidence = models.FileField(upload_to='complaints/')
    status = models.CharField(max_length=20,default="Pending")