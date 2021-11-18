from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name