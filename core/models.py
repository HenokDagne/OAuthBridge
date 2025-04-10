from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# filepath: c:\Users\hp\OneDrive\Desktop\DjangoProject\Advanced Authentication\Authentication\core\models.py

class CustomUser(AbstractUser):
    # Add any additional fields you want to include in your custom user model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='image/', blank=True, default='image/download.jpg')
    
    
    




        

