from django.urls import (path, include)
from . views import menu_view

urlpatterns = [
    path('', menu_view, name='home')
]
