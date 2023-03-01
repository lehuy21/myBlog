from django.db import models
# Create your models here.
class Usermodel(models.Model):
    name = models.CharField(max_length=100, name="name")
    email = models.EmailField(max_length=100, name="email")
    phone = models.CharField(max_length=50, name="phone")
    message = models.TextField(max_length=1000, name="message")
    birthday = models.DateTimeField(auto_now_add=True, name="birthday")
    address = models.CharField(max_length=2000, name="address")