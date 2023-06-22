from django.urls import (path, include)
from . views import (home, service, menu_view_2, menu_view_3, about)

urlpatterns = [
    path('', home, name='home'),
    path('services', service, name='service'),
    path('abouts', about, name='about'),
    path('services/design', menu_view_2, name='design'),
    path('services/design/html', menu_view_3, name='html'),
    path('services/develop', menu_view_3, name='develop'),
    path('services/graphic', menu_view_3, name='graphic'),
    path('services/graphic/logo', menu_view_3, name='logo'),
    path('services/graphic/banner', menu_view_3, name='banner'),
]
