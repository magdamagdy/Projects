from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse , resolve
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from django.core.management import call_command
from reg.models import *
from reg.views import *


class TestRegViews(TestCase):
    def setUp(self):
        self.client = Client()
    #
    # def test_reg(self):
    #     response = self.client.post(reverse("reg")), {
    #         'username': 'Michael',
    #         'email': 'michael123@yahoo.com',
    #         'password': '123456',
    #         'password1': '123456',
    #         'check': 'Buyer'
    #     }
    #     self.assertEqual(response.status_code, 200)


