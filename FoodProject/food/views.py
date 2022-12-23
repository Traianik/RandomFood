from django.shortcuts import render
from django.template import loader

# Create your views here.

food_list = [
        {'id':1, 'name':'Burger King'},
        {'id':2, 'name':'Andys Pizza'},
        {'id':3, 'name':'McDonalds'},

]

def index(request):
        context = {'food_list':food_list}
        return render(request,'food/index.html',context)