from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class type_of_customer(models.Model):
    username = models.CharField(max_length=30)
    type = models.CharField(max_length=10)