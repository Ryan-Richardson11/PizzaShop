from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Menu

# Create your views here.


def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


# redirects to admin login page
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

# returns all the names of menu items


def menu_list(request):
    menu_items = Menu.objects.all()
    return render(request, 'home/menu_list.html', {'menu': menu_items})


def menu_item_info(request, pk):
    try:
        item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        raise Http404('Item does not exist')
    return render(request, 'home/item_detail.html', {'item': item})
