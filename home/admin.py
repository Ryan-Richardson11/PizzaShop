from django.contrib import admin
from . import models

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('pizza_type',)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)


class CartItemAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Topping, ToppingAdmin)
admin.site.register(models.Size, SizeAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
