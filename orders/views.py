from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import MenuItem, Order, OrderItem
from django.core import serializers
import json

# Create your views here.
def index(request):
    # Exclude Toppings
    menuItems = {}
    itemCategory = MenuItem.objects.values_list('itemCategory', flat=True).distinct()
    for ic in itemCategory:
        subCategory = MenuItem.objects.filter(itemCategory=ic).values_list('itemSubCategory', flat=True).distinct()
        #print(f"Subcategories:{subCategory}")
        itemDict ={}
        for sc in subCategory:
            #itemGroup = MenuItem.objects.exclude(itemSubCategory="Toppings").filter(itemCategory=ic, itemSubCategory=sc).values_list('itemGroup', flat=True).distinct()
            items=  MenuItem.objects.exclude(itemSubCategory="Toppings").filter(itemCategory=ic,itemSubCategory=sc)
            itemDict[sc] = items
            menuItems[ic]=itemDict

    # Include Only Toppings
    Toppings = {}
    items=  MenuItem.objects.filter(itemSubCategory="Toppings")
    Toppings=items

    context = {'menuItems':menuItems, 'toppings':Toppings}
    return render(request, "orders/order.html", context)
    #return HttpResponse(menuItems)