from django.urls import (path, include)
from . views import (home, service, menu_view_2, menu_view_3, about)

urlpatterns = [
    path('home', home, name='home'),
    path('service', service, name='service'),
    path('about', about, name='about'),
    path('de', menu_view_2, name='design'),
    path('service', menu_view_3, name='service'),
    path('service', menu_view_3, name='html'),
    path('service', menu_view_3, name='develop')
]
