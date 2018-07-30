from django.db import models

# Create your models here.
class MenuItem(models.Model):
    itemCategory = models.CharField(max_length=200)
    itemSubCategory = models.CharField(max_length=200)
    itemName = models.CharField(max_length=200)
    itemGroup = models.CharField(max_length=200)
    unitPrice = models.FloatField()
    SIZES =( ('S', 'Small'),
             ('L', 'Large'),
             ('N', 'NA')
        )
    itemSize = models.CharField(max_length=1, choices=SIZES)
    noOfTopping = models.IntegerField()

    def __str__(self):
        return f"{self.itemSubCategory}:{self.itemName}({self.itemSize}) @ {self.unitPrice}"


class Order(models.Model):
    STATUS = (
        ('N','NotOrderedYet'),
        ('O', 'Ordered'),
        ('I', 'Cooking'),
        ('R', 'Ready'),
        ('D', 'Delivered')
        )
    userID  = models.IntegerField()
    orderStatus = models.CharField(max_length=1, choices=STATUS)
    order_date = models.DateTimeField('Ordered date')
    totalPrice = models.FloatField()

    def __str__(self):
        return f"{self.userID}({self.orderStatus}) @ {self.totalPrice}"

class OrderItem(models.Model):
    itemID = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItems' )

    def __str__(self):
        return f"{self.itemID}:{self.quantity} - {self.price}"
