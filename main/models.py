from django.db import models

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['mTitle']) < 5:
            errors["title"] = "TV Show Title should be at least 5 characters long"
        if len(postData['mNetwork']) < 2:
            errors["network"] = "TV Show Network should be at least 2 characters long"
        if len(postData['mDescription']) < 10:
            errors["description"] = "TV Show description should be at least 10 characters long"
        return errors



# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=90)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()