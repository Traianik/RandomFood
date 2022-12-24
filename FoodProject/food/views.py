from django.shortcuts import render
from django.template import loader
import random
# Create your views here.

def generate_food():
        food_list = [
                {'food_name':'Pizza', 'food_description':'Pizza is a wonderfull!'},
                {'food_name':'Potatoes', 'food_description':'Potates are fires!'},
                {'food_name':'Burger', 'food_description':'Burget is burger king!'},
        ]

        random_food = random.choice(food_list)
        return random_food 
 
 
def index(request):
        random_food = generate_food()
        context = {'random_food':random_food}  
        return render(request,'food/index.html',context)