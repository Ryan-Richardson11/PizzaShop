from django.db import models

# Stores different types of toppings in the database


class Topping(models.Model):
    name = models.CharField(max_length=50)

# Stores different menu items in the database


class Menu(models.Model):
    pizza_type = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping, blank=True)
    size = models.CharField(max_length=50, default='Large')
    description = models.TextField()

# class Cart(models.Model):
    # order_time = models.DateTimeField(auto_now_add=True)
#     pass
