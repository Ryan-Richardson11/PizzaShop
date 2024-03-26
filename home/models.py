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
    image_url = models.URLField(blank=True, null=True)


class CartItem(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_size = models.ForeignKey(Size, on_delete=models.CASCADE)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
