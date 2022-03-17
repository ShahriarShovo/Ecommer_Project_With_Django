from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from App_Shop.models import Product
from App_Shop.models import Category

# Create your views here.


class Home(ListView):
    model= Product
    template_name='App_Shop/home.html'

class Product_Details(DetailView):
    model= Product
    template_name='App_Shop/product_details.html'

class Category(ListView):
    model= Category
    template_name='App_Shop/category_list.html'

    
def show_Category_Wise(request,pk):
    object_list=Product.objects.filter(category=pk)
    return render(request,'App_Shop/show_category_wise.html', context={'object_list':object_list})

  
