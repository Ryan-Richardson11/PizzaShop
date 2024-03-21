from django.db import models

# Stores different types of toppings in the database


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=25)

# Stores different menu items in the database


class Menu(models.Model):
    pizza_type = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping, blank=True)
    description = models.TextField()

# class Cart(models.Model):
    # order_time = models.DateTimeField(auto_now_add=True)
#     pass
