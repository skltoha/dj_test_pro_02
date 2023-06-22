from django.urls import (path, include)
from . views import (home, service, about)

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', service, name='service'),
]
