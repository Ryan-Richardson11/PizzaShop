from django.db import models

# Create your models here.


class Menu(models.Model):
    pizza_type = models.CharField(max_length=50)
    toppings = models.CharField(max_length=50)
    description = models.TextField()

# class Toppings(models.Model):
#     pass


# class Cart(models.Model):
    # order_time = models.DateTimeField(auto_now_add=True)
#     pass
