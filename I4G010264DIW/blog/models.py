from django.db import models
from django.contrib.auth import get_user_model
import datetime
User=get_user_model()
Created_date=datetime.date(2022, 6, 15)
# Create your models here.
class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Text= models.TextField()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
    def __str__(self):
        return self.Title