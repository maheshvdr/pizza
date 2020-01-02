from __future__ import unicode_literals
from django.shortcuts import render
from django.http import request,HttpResponse
from pizza_config.settings import TIME_ZONE
from pizza_app.models import PizzaType,Pizza,Transactions
from django.db.models import Sum,Count

import pytz
from django.utils import timezone

def index(request):
    time_zone = TIME_ZONE
    timezone.activate(pytz.timezone(time_zone))
    time_zone = str(timezone.now())

    total_sold_amount=Transactions.objects.aggregate(total_sold_amount=Sum('pizza_amount'))
    total_sold_pizzas=Transactions.objects.values('pizza_id').count()
    print(total_sold_pizzas)
    pizzas_sold_count=Transactions.objects.values('pizza_id').annotate(total_sold_pizzas=Sum('pizza_amount')).order_by('-total_sold_pizzas')
    all_pizza=[]
    for index,pizza in enumerate(pizzas_sold_count):
        pizza.update({'pizza_name':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().name,
                      'pizza_type':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().pizza_type_id.name,
                      'price':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().price})
        all_pizza.append(pizza)


    return  render(request,'index.html',{'all_pizza':all_pizza,'total_sold_pizzas':total_sold_pizzas,'total_sold_amount':total_sold_amount,'time_zone':time_zone})
    
    