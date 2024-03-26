from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
    path('menu', views.menu_list, name="menu.list"),
    path('menu/<int:pk>', views.menu_item_info, name="menu.detail"),
    path('cart', views.view_cart, name="cart.items"),
    path('menu/<int:pk>/add_to_cart/',
         views.add_to_cart, name='add_to_cart'),
]
