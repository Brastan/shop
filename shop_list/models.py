from django.db import models

# Create your models here.

class Tag(models.Model):
  tag_name = models.CharField(max_length=20)
 
  def __str__(self):
      return self.tag_name

class Item(models.Model):
  item_name = models.CharField(max_length=70)
  item_price = models.FloatField()
  item_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, related_name='item')

  def __str__(self):
      return f"{self.item_name }......  R{self.item_price} "
