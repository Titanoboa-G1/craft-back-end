# from django.contrib.auth.models import User
from django.test import TestCase
# from django.conf import settings
from django.contrib.auth import get_user_model

from craft.models import Category, Product

"""Testing Models"""
# User = settings.AUTH_USER_MODEL
# User = get_user_model()


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), "django")


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name="django", slug="django")
        get_user_model().objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            created_by_id=1,
            title="django test",
            price="10.00",
            image="django",
        )

    def test_products_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django test")


"""Testing Views"""
from django.contrib.auth.models import User
# from unittest import skip
from django.test import Client, TestCase
from django.urls import reverse

# @skip
# class TestSkip(TestCase):
#     def test_skip_expample(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name="django", slug="django")
        get_user_model().objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            created_by_id=1,
            title="django test",
            price="10.00",
            image="django",
        )

    def test_url_allowed_hosts(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

