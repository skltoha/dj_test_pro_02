from django.contrib import admin
from .models import Menu


class menulist(admin.ModelAdmin):
    list_display = [field.name for field in Menu._meta.fields]

admin.site.register(Menu, menulist)

