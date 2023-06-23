from django.contrib import admin
from .models import product, Image

# Register your models here.
class productlist(admin.ModelAdmin):
    list_display = [field.name for field in product._meta.fields]

admin.site.register(product, productlist)

class imagelist(admin.ModelAdmin):
    list_display = [field.name for field in Image._meta.fields]

admin.site.register(Image, imagelist)
