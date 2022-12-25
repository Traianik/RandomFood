from django.shortcuts import render
from django.template import loader
from random import choice
from .models import FoodData


def generate_food():
 

        pks = FoodData.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_obj = FoodData.objects.get(pk=random_pk)
        print(random_obj)
        return random_obj

 
def index(request):
        random_food = generate_food()
        context = {'random_food':random_food}   
        return render(request,'food/index.html',context)