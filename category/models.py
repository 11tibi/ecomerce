from django.db import models

# Create your models here.


class Categories(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.name
