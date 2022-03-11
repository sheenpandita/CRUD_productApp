from django.db import models

# Create your models here.
class pro(models.Model):
    item_name = models.CharField(max_length=70)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images')
