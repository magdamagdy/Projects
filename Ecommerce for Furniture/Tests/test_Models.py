from django.test import TestCase
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from django.core.management import call_command
from cart.models import *
from dashboard.models import *
from reg.models import *
from home.models import *
from recommend.models import *


# Cart Models 5 tests

class TestCartModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="Michael", email="michael@yahoo.com")
        self.user2 = User.objects.create(username="Marshall", email="marshall@yahoo.com")
        self.add_to_cart = Add_to_cart.objects.create(user=self.user1, username=self.user1.username, product_id="45",
                                                      description="chair", product_quantity=3, image="dashboard/c4.jpg",
                                                      price=150, total=300, quantity=2)
        self.total_user = Total_for_user.objects.create(user=self.user1, amount_paid=300, product_id="45",
                                                        quantity_ordered=2)
        self.total1 = Total.objects.create(user=self.user1, total=300)
        self.checkout = checkout_details(username=self.user1.username, email=self.user1.email, phone=1234,
                                         address="221B", country="Egypt", currency="L.E", city="cairo",
                                         paymentMethod="Visa")
        self.participation = User_participation.objects.create(user=self.user1, count=10)

    def test_add_to_cart(self):
        self.assertEqual(self.add_to_cart.user, self.user1)
        self.assertEqual(self.add_to_cart.username, "Michael")
        self.assertEqual(self.add_to_cart.product_id, "45")
        self.assertNotEqual(self.add_to_cart.description, "Table")
        self.assertEqual(self.add_to_cart.product_quantity, 3)
        self.assertEqual(self.add_to_cart.image, "dashboard/c4.jpg")
        self.assertEqual(self.add_to_cart.price, 150)
        self.assertNotEqual(self.add_to_cart.total, 150)
        self.assertNotEqual(self.add_to_cart.quantity, 4)

    def test_total_user(self):
        self.assertEqual(self.total_user.user, self.user1)
        self.assertEqual(self.total_user.amount_paid, 300)
        self.assertEqual(self.total_user.product_id, "45")
        self.assertNotEqual(self.total_user.quantity_ordered, 5)

    def test_total(self):
        self.assertEqual(self.total1.user, self.user1)
        self.assertNotEqual(self.total1.total, 250)

    def test_checkout(self):
        self.assertEqual(self.checkout.username, "Michael")
        self.assertEqual(self.checkout.email, "michael@yahoo.com")
        self.assertEqual(self.checkout.phone, 1234)
        self.assertEqual(self.checkout.address, "221B")
        self.assertNotEqual(self.checkout.country, "Brazil")
        self.assertNotEqual(self.checkout.currency, "$")
        self.assertNotEqual(self.checkout.city, "Rio")
        self.assertNotEqual(self.checkout.paymentMethod, "Cash")

    def test_participation(self):
        self.assertNotEqual(self.participation.user, self.user2)
        self.assertEqual(self.participation.count, 10)

# Dashboard Models 1 test


class TestDashboardModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="Michael", email="michael@yahoo.com")
        self.user2 = User.objects.create(username="Marshall", email="marshall@yahoo.com")
        self.additem = Additem.objects.create(user=self.user2, image="dashboard/c4.jpg", description="chair", price=50,
                                              amount=2, category="chairs")
# Ask Marina or Majda about time

    def test_add_item(self):
        self.assertEqual(self.additem.user, self.user2)
        self.assertEqual(self.additem.image, "dashboard/c4.jpg")
        self.assertEqual(self.additem.description, "chair")
        self.assertNotEqual(self.additem.price, 60)
        self.assertEqual(self.additem.amount, 2)
        self.assertNotEqual(self.additem.category, "sofas")


# Home Models  5 tests

class TestHomeModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="Michael", email="michael@yahoo.com")
        self.user2 = User.objects.create(username="Marshall", email="marshall@yahoo.com")
        self.wish = Whishlist.objects.create(image="dashboard/c4.jpg", description="tables", price=30,
                                             user=self.user1, old_id=21)
        self.reviews = Reviews.objects.create(item_id=24, review="Excellent", img="dashboard/c4.jpg", category="tables")
        self.rating1 = Rating.objects.create(item_id=24, rating=30, user_id=14, img="dashboard/c4.jpg",
                                             category="tables")
        self.seller_rating = Seller_rating.objects.create(user_id=24, rating=50)
        self.product_rating = Product_rating.objects.create(item_id=24, rating=50, img="dashboard/c4.jpg",
                                                            category="tables")

    def test_wish(self):
        self.assertEqual(self.wish.image, "dashboard/c4.jpg")
        self.assertNotEqual(self.wish.description, "chairs")
        self.assertEqual(self.wish.price, 30)
        self.assertNotEqual(self.wish.user, self.user2)
        self.assertEqual(self.wish.old_id, 21)

    def test_reviews(self):
        self.assertEqual(self.reviews.img, "dashboard/c4.jpg")
        self.assertNotEqual(self.reviews.review, "Very Good")
        self.assertEqual(self.reviews.category, "tables")
        self.assertNotEqual(self.reviews.item_id, 30)

    def test_rating(self):
        self.assertEqual(self.rating1.rating, 30)
        self.assertEqual(self.rating1.category, "tables")
        self.assertEqual(self.rating1.user_id, 14)
        self.assertNotEqual(self.rating1.item_id, 30)
        self.assertNotEqual(self.rating1.img, "dashboard/c3.jpg")

    def test_seller_rating(self):
        self.assertEqual(self.seller_rating.user_id, 24)
        self.assertNotEqual(self.seller_rating.rating, 24)

    def test_product_rating(self):
        self.assertEqual(self.product_rating.rating, 50)
        self.assertEqual(self.product_rating.category, "tables")
        self.assertNotEqual(self.product_rating.item_id, 30)
        self.assertNotEqual(self.product_rating.img, "dashboard/c3.jpg")


# Reg Models 1 test

class TestRegModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="Michael", email="michael@yahoo.com")
        self.user2 = User.objects.create(username="Marshall", email="marshall@yahoo.com")
        self.type = type_of_customer.objects.create(username=self.user1.username, type="seller")

    def test_type_of_customer(self):
        self.assertEqual(self.type.username, self.user1.username)
        self.assertEqual(self.type.type, "seller")
        self.assertNotEqual(self.type.username, self.user2.username)
        self.assertNotEqual(self.type.type, "buyer")


# Recommend Models 1 test
class TestRecommendModels(TestCase):
    def setUp(self):
        self.save1 = save_products.objects.create(description="Great", price=150, image="dashboard/c4.jpg")

    def test_save_products(self):
        self.assertEqual(self.save1.description, "Great")
        self.assertEqual(self.save1.price, 150)
        self.assertNotEqual(self.save1.image, "dashboard/c3.jpg")

