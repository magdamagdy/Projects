from django.test import TestCase
from django.urls import reverse, resolve
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from django.core.management import call_command
from reg.models import *
from home.views import *
from dashboard.views import *
from reg.views import *
from cart.views import *
from recommend.views import *

# Recommend Urls 1 test
class RecommendTest(TestCase):
    def test_recommendation(self):
        url = reverse("recommendation")
        self.assertEqual(resolve(url).func, recommendation)

# Cart Urls 7 tests


class CartTest(TestCase):
    def test_show_items(self):
        url = reverse("show_items")
        self.assertEqual(resolve(url).func, show_items)

    def test_offers(self):
        url = reverse("offers")
        self.assertEqual(resolve(url).func, offers)

    def test_checkout(self):
        url = reverse("checkout")
        self.assertEqual(resolve(url).func, checkout)

    def test_confirm(self):
        url = reverse("confirm")
        self.assertEqual(resolve(url).func, confirm)

    def test_add_to_cart(self):
        url = reverse("add_to_cart", args=['1'])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_add_quantity(self):
        url = reverse("add_quantity", args=['1'])
        self.assertEqual(resolve(url).func, add_quantity)

    def test_remove_cart(self):
        url = reverse("remove_cart", args=['1'])
        self.assertEqual(resolve(url).func, remove_cart)


# Dashboard Urls 2 tests


class DashboardTest(TestCase):
    def test_dashboard(self):
        url = reverse("dashboard")
        self.assertEqual(resolve(url).func, dashboard)

    def test_remove_item(self):
        url = reverse("remove_item", args=['1'])
        self.assertEqual(resolve(url).func, remove_item)

# Home Urls 23 tests


class HomeTest(TestCase):
    def test_home(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_reg(self):
        url = reverse("reg")
        self.assertEqual(resolve(url).func, reg)

    def test_log(self):
        url = reverse("log")
        self.assertEqual(resolve(url).func, log)

    def test_chairs(self):
        url = reverse("chairs")
        self.assertEqual(resolve(url).func, chairs)

    def test_seller(self):
        url = reverse('seller')
        self.assertEqual(resolve(url).func, seller)

    def test_buyer(self):
        url = reverse('buyer')
        self.assertEqual(resolve(url).func, buyer)

    def test_armchairs(self):
        url = reverse('armchairs')
        self.assertEqual(resolve(url).func, armchairs)

    def test_sofas(self):
        url = reverse('sofas')
        self.assertEqual(resolve(url).func, sofas)

    def test_beds(self):
        url = reverse('beds')
        self.assertEqual(resolve(url).func, beds)

    def test_chaiselognues(self):
        url = reverse('chaiselongues')
        self.assertEqual(resolve(url).func, chaiselongues)

    def test_shelving(self):
        url = reverse('shelving_units')
        self.assertEqual(resolve(url).func, shelving_units)

    def test_tables(self):
        url = reverse('tables')
        self.assertEqual(resolve(url).func, tables)

    def test_wardrobes(self):
        url = reverse('wardrobes')
        self.assertEqual(resolve(url).func, wardrobes)

    def test_whishlist(self):
        url = reverse('whishlist')
        self.assertEqual(resolve(url).func, whishlist)

    def test_remove_from_wish(self):
        url = reverse("remove_from_wish", args=['1'])
        self.assertEqual(resolve(url).func, remove_from_wish)

    def test_rating_review_chairs(self):
        url = reverse("rating_review_chairs", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_chairs)

    def test_rating_review_armchairs(self):
        url = reverse("rating_review_armchairs", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_armchairs)

    def test_rating_review_sofas(self):
        url = reverse("rating_review_sofas", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_sofas)

    def test_rating_review_beds(self):
        url = reverse("rating_review_beds", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_beds)

    def test_rating_review_chaiselongues(self):
        url = reverse("rating_review_chaiselongues", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_chaiselongues)

    def test_rating_review_wardrobes(self):
        url = reverse("rating_review_wardrobes", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_wardrobes)

    def test_rating_review_shelving_units(self):
        url = reverse("rating_review_shelving_units", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_shelving_units)

    def test_rating_review_tables(self):
        url = reverse("rating_review_tables", args=['1'])
        self.assertEqual(resolve(url).func, rating_review_tables)

    def test_Chairs(self):
        url = reverse("Chairs", args=["1"])
        self.assertEqual(resolve(url).func, Chairs)

    def test_Armchairs(self):
        url = reverse('Armchairs', args=["1"])
        self.assertEqual(resolve(url).func, Armchairs)

    def test_Sofas(self):
        url = reverse('Sofas', args=["1"])
        self.assertEqual(resolve(url).func, Sofas)

    def test_Beds(self):
        url = reverse('Beds', args=["1"])
        self.assertEqual(resolve(url).func, Beds)

    def test_Chaiselognues(self):
        url = reverse('Chaiselongues', args=["1"])
        self.assertEqual(resolve(url).func, Chaiselongues)

    def test_Shelving(self):
        url = reverse('Shelving_units', args=["1"])
        self.assertEqual(resolve(url).func, Shelving_units)

    def test_Tables(self):
        url = reverse('Tables', args=["1"])
        self.assertEqual(resolve(url).func, Tables)

    def test_Wardrobes(self):
        url = reverse('Wardrobes', args=["1"])
        self.assertEqual(resolve(url).func, Wardrobes)


# Reg Urls 2 tests


class RegTest(TestCase):
    def test_reg(self):
        url = reverse("reg")
        self.assertEqual(resolve(url).func, reg)

    def test_log(self):
        url = reverse("log")
        self.assertEqual(resolve(url).func, log)










