
from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from App_Shop.models import Product

def index(request):
    return HttpResponseRedirect(reverse('App_Shop:home'))


def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'product-search.html', {"results":results})

    return render(request, 'product-search.html')




