from django.db import models
from django.utils import timezone

# Create your models here.
class bug(models.Model):
    title = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()


def __str__(self):
    return self.title
