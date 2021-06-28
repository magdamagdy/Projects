from django.db import models
from django.contrib.auth.models import auth, User
# Create your models here.
from dashboard.models import Additem


class Whishlist (models.Model):
    image = models.ImageField(upload_to="whishlist", blank=True, null=True)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    old_id = models.IntegerField()


class Reviews (models.Model):
    item_id = models.IntegerField()
    review = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="reviews", blank=True, null=True)
    category = models.CharField(max_length=70)

class Rating (models.Model):
    item_id = models.IntegerField()
    rating = models.IntegerField()
    user_id = models.IntegerField()
    img = models.ImageField(upload_to="reviews", blank=True, null=True)
    category= models.CharField(max_length=70)

class Seller_rating (models.Model):
    user_id = models.IntegerField()
    rating = models.IntegerField()

class Product_rating (models.Model):
    item_id = models.IntegerField()
    img = models.ImageField(upload_to="reviews", blank=True, null=True)
    rating = models.IntegerField()
    category = models.CharField(max_length=70)