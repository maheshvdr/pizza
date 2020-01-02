# -*- coding: utf-8 -*-
from pizza_app.models import Pizza,PizzaType,Transactions
from django.core.management.base import BaseCommand,CommandError
import random

class Command(BaseCommand):
    
    def handle(self,*args,**options):
        pizza_types=[1,2,3]
        random_pizza_name = ['california','chicago','new york']

        # insert pizza type if not exist. Its first time
        if(PizzaType.objects.filter().count()<3):
            try:
                for i in range(len(pizza_types)):
                    new_pizza_type=PizzaType()
                    new_pizza_type.name=random_pizza_name[i]
                    new_pizza_type.save()
            except CommandError as err:
                print(err.args)
        
        
        del pizza_types[:]
        pizzT=PizzaType.objects.filter()
        for p in pizzT:
            pizza_types.append(p.pizza_type_id)

        random_pizza_type=PizzaType.objects.filter(pizza_type_id=random.choice(pizza_types)).first()
        random_price=random.randrange(10.00,100.00)
        random_price_delivery=random.randrange(10,20)
        # insert pizza

        pizza_order_name = ['mahesh','rahu', 'sachin', 'jack ma', 'jeni']

        try:
            new_pizza=Pizza()
            new_pizza.name=random.choice(pizza_order_name)
            new_pizza.pizza_type_id=random_pizza_type
            new_pizza.price=random_price
            new_pizza.save()

            print('insert random pizza data one row.')

            random_pizza = Pizza.objects.filter().last()
            
            try:
                new_transaction=Transactions()
                new_transaction.pizza_id = random_pizza
                new_transaction.pizza_amount=random_price + random_price_delivery
                new_transaction.price=random_price
                new_transaction.save()
                print('insert random pizza transaction data one row.')

            except CommandError as err:
                print(err.args)

        except CommandError as err:
            print(err.args)
