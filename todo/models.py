from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
   
    title = models.CharField(max_length=122)
    created = models.DateTimeField(auto_now_add=True)
    priority =  models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']