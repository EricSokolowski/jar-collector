from django.db import models
from django.urls import reverse
from datetime import date

PRODUCTS = (
  ('W', 'Windex'),
  ('I', 'Invisible Glass'),
  ('G', 'Glass Plus')
)

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

  def fed_for_today(self):
    return self.cleaning_set.filter(date=date.today()).count() >= len(PRODUCTS)

class Cleaning(models.Model):
  date = models.DateField('Cleaning date')
  product = models.CharField(
    max_length=1,
    choices=PRODUCTS,
    default=PRODUCTS[0][0]
    )
  jar = models.ForeignKey(Jar, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_product_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Sticker(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('stickers_detail', kwargs={'pk': self.id})
    