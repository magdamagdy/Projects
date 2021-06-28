from django.test import TestCase
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from django.core.management import call_command
from dashboard.models import *
from dashboard.forms import *

# DashBoard Froms 2 tests


class TestForm(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="Michael", email="michael@yahoo.com")
        self.additem = Additem.objects.create(user=self.user1, image="dashboard/c4.jpg", description="chair", price=50,
                                              amount=2, category="chairs")

    def test_form_valid(self):
        form = AdditemForm(data={
            'image': self.additem.image,
            'description': self.additem.description,
            'price': self.additem.price,
            'amount': self.additem.amount,
            'category': self.additem.category
        })
        self.assertTrue(form.is_valid())

    def test_form_missing_Data(self):
        form = AdditemForm(data={
            'image': self.additem.image,
            'description': self.additem.description,
            'category': self.additem.category
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


