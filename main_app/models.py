from django.db import models

from django.urls import reverse

# Create your models here.
class Jar(models.Model):
  name = models.CharField(max_length=100)
  contents = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField(default = 1)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("jars_detail", kwargs={"jar_id": self.id})
