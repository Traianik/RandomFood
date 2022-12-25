from django.contrib import admin
from .models import FoodData

class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('id',) 
    

admin.site.register(FoodData,FoodAdmin)  