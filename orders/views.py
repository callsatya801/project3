from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import MenuItem, Order, OrderItem
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

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

    # Include Only Pizza Toppings
    pizza_toppings = {}
    items=  MenuItem.objects.filter(itemCategory="Pizza", itemSubCategory="Toppings").values_list('id','itemName','unitPrice')
    pizza_toppings= json.dumps(list(items), cls=DjangoJSONEncoder)
    print(pizza_toppings)

    # Include Only Subs Toppings
    subs_toppings = {}
    items=  MenuItem.objects.filter(itemCategory="Subs", itemSubCategory="Toppings").values_list('id','itemName','unitPrice')
    subs_toppings= json.dumps(list(items), cls=DjangoJSONEncoder)
    print(subs_toppings)


    context = {'menuItems':menuItems, 'p_toppings':pizza_toppings, 's_toppings':subs_toppings }
    return render(request, "orders/order.html", context)
    #return HttpResponse(menuItems)