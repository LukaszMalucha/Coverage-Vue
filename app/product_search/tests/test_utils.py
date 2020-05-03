from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import MyProfile
from core.models import ProductModel, DocumentModel, TopicModel
from product_search.utils import clean_brand_list, get_brand_name, reverse_brand_name, BRAND_MAPPER


class GetBrandListTest(TestCase):

    def test_clean_brand_list(self):
        test_list = clean_brand_list(["ANSUL", "TYCO FIRE", "Not Specified"])
        self.assertEqual(test_list, ["ansul", "tyco-fire"])


class GetBrandNameTest(TestCase):

    def test_get_brand_name_in(self):
        test_name = get_brand_name("fireater")
        self.assertEqual(test_name, "FIREATER")

    def test_get_brand_name_not_in(self):
        test_name = get_brand_name("asd")
        self.assertEqual(test_name, "asd")


class ReverseBrandNameTest(TestCase):

    def test_reverse_brand_name_in(self):
        test_name = reverse_brand_name("FIREATER")
        self.assertEqual(test_name, "fireater")


    def test_reverse_brand_name_not_in(self):
        test_name = reverse_brand_name("asd")
        self.assertEqual(test_name, "johnson-controls")

