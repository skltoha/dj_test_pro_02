from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name