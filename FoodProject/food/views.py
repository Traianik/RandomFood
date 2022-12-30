from django.shortcuts import render,HttpResponse
from django.template import loader
from random import choice
from .models import FoodData
from django.contrib.auth.forms import UserCreationForm

def generate_food():
        #get random value from db
        pks = FoodData.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_obj = FoodData.objects.get(pk=random_pk)
        print(random_obj)

        #making sure that is not repeating

        return random_obj

def food_page(request):
        random_food = generate_food()
        context = {'random_food':random_food}   
        return render(request,'food/food_page.html',context)