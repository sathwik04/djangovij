from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (

        ('ROOM RENT', 'Room Rent'),
        ('Maintance', 'Maintance'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)


    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.customer)

class Order(models.Model):

    STATUS = (
        ('Assigned', 'Assigned'),
    )
    STATUS1 = (
        ('Dish washes', 'Dish washes'),
        ('House Cleaning','House Cleaning'),
        ('WaterCAn', 'WaterCAn'),
        ('Washroom Cleaning', 'Washroom Cleaning',),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    works = models.CharField(max_length=200, null=True, choices=STATUS1)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer)

class Bills(models.Model):
    STATUS2 = (
        ('RicePacket', 'Ricepacket'),
        ('Watercans', 'Watercans'),
        ('Curries', 'Curries'),
        ('WifiBill', 'WifiBill',),
        ('Rommproducts', 'Roomproducts',),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    bills=models.CharField(max_length=120,null=True,choices=STATUS2)
    price = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.customer)


