from django.db import models

# Create your models here.
class Commands(models.Model):
    command1 = models.CharField(max_length=200)
    command2 = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    
def __str__(self):
    return str(self.lesson)