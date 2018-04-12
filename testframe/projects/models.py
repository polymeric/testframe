from django.db import models

# Create your models here.
class Projects(models.Model):
  name = models.CharField(max_length=64)
  created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
  description = models.TextField(blank=True)
  archived = models.BooleanField(default=False)