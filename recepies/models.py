from django.db import models

# Create your models here.


class Receipe(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.name    