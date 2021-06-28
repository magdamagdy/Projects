from django.db import models
from django.contrib.auth.models import auth, User
from django import forms
# Create your models here.
class Additem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    #user_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dashboard", blank=True, null=True)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=70,
    choices=[
      ('chairs', 'Chairs'),
      ('armchairs', 'Armchairs'),
      ('chaiselongues', 'Chaiselongues'),
      ('sofas', 'Sofas'),
      ('wardrobes', 'Wardrobes'),
      ('beds', 'Beds'),
      ('shelving units', 'Shelving Units'),
      ('tables', 'Tables'),
     ]
    )

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.user.id