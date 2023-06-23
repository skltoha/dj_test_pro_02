from django.db import models
from menu.models import Menu


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name
    
    
class product(models.Model):
    name        = models.CharField(max_length=50, null=False, blank=False)
    details     = models.CharField(max_length=1000, null=True, blank=True)
    price       = models.IntegerField(null=True, blank=True)
    discount    = models.IntegerField(null=True, blank=True)
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE)
    images      = models.ManyToManyField(Image)
    
    def __str__(self):
            return self.name
        
