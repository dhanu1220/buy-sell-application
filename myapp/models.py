from django.db import models

class Product(models.Model):
    def __str__(self):
        return self.name #return name of product instead of product1 product2
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')
    
