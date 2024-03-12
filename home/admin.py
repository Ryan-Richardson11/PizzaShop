from django.contrib import admin
from . import models

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('pizza_type',)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Topping, ToppingAdmin)
