from django.db import models
from authapp.models import *
# Create your models here.
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_favourite=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)