from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    is_verified=models.BooleanField(default=False)
    verification_token=models.UUIDField(default=uuid.uuid4,unique=True)