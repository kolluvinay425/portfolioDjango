from django.db import models

# Create your models here.
class Project(models.Model):

    links = models.CharField(max_length=200,default='null')

    def __str__(self):
        return self.links

