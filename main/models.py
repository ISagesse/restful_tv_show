from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=90)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)