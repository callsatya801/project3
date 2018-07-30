from django.db import models

# Create your models here.
class MenuItems(models.Model):
    ItemCategory = models.CharField(max_length=200)
    ItemName = models.CharField(max_length=)
    ItemName = models.CharField(max_length=200)
    ItemSize = models.CharField(max_length=200)
    ItemGroup = models.CharField(max_length=200)
    UnitPrice = models.FloatField()
    SIZES =( ('S', 'Small'),
             ('L', 'Large'),
             ('N', 'NA')
        )
    ItemSize = models.CharField(max_length=1, choices=SIZES)
    NoOfTopping = models.IntegerField()

Class Order