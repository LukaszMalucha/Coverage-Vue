from django.test import TestCase

from document_search.apps import DocumentSearchConfig


class DocumentSearchConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(DocumentSearchConfig.name, "document_search")
