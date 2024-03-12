from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
    path('menu', views.menu_list),
    path('menu/<int:pk>', views.menu_item_info),
]
