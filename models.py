from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
