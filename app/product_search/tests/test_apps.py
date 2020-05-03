from django.test import TestCase

from product_search.apps import ProductSearchConfig


class DocumentSearchConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(ProductSearchConfig.name, "product_search")
