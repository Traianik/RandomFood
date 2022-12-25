from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class FoodData(models.Model):
    food_name = models.CharField(max_length=200) 
    food_description = HTMLField(null=True,default="INGREDIENTS:<br><br><br>RECIPE:")
    food_image = models.ImageField(upload_to='media', default='media/dish.png')   