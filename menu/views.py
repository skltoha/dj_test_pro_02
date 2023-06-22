from django.shortcuts import render, redirect
from .models import Menu

def home(request):
    menu_items = Menu.objects.all() # Retrieve all menu items from the database
    msg = f'web menu home'
    context = {
        'menu_items': menu_items,
        'msg': msg
    }
    return render(request, 'menu.html', context)


def service(request):
    menu_items = Menu.objects.all()  # Retrieve all menu items from the database
    msg = f'web menu service'
    context = {
        'menu_items': menu_items,
        'msg': msg
    }
    return render(request, 'menu.html', context)

def about(request):
    menu_items = Menu.objects.all()  # Retrieve all menu items from the database
    msg = f'web menu about'
    context = {
        'menu_items': menu_items,
        'msg': msg
    }
    return render(request, 'menu.html', context)

