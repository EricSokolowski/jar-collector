from django.db import models

# Create your models here.
class Jar(models.Model):
  name = models.CharField(max_length=100)
  contents = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  type = models.CharField(max_length=100)


  def __str__(self):
    return self.name
