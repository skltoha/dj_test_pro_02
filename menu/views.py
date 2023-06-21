from django.shortcuts import render
from .models import Menu

def menu_view(request):
    menu_items = Menu.objects.all()  # Retrieve all menu items from the database
    return render(request, 'menu.html', {'menu_items': menu_items})
