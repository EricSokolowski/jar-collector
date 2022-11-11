from django.db import models

# Create your models here.
class Jar(models.Model):
  name = models.CharField(max_length=100)
  contents = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField(default = 1)


  def __str__(self):
    return self.name
