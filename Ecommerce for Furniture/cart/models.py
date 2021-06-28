from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Add_to_cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=20)
    product_id = models.CharField(max_length=100000)
    description = models.CharField(max_length=1000)
    product_quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='cart')
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)






class Total_for_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    amount_paid = models.FloatField(default=0)  #quantity*price
    product_id = models.CharField(max_length=100000)
    quantity_ordered = models.IntegerField(default=1)


class Total(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    total = models.FloatField()

class checkout_details(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    paymentMethod = models.CharField(max_length=10)



class User_participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    count = models.IntegerField(default=0)