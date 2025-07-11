from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f'{self.name}{self.course}'
