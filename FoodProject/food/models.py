from django.db import models

# Create your models here.
class FoodData(models.Model):
    food_name = models.CharField(max_length=200) 
    food_description = models.TextField(null=True,blank=True,default="No description added.")
    food_image = models.ImageField(upload_to='media', default='media/dish.png')  