from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProductModel, DocumentModel, TopicModel
from product_search.serializers import ProductModelSerializer

DASHBOARD_URL = reverse("analytics:dashboard")



def sample_superuser():
    user = get_user_model().objects.create_superuser(
        email="superuser@gmail.com",
        password="test1234",
    )
    return user


def sample_user():
    user = get_user_model().objects.create_user(
        email="user@gmail.com",
        password="test1234",
    )
    return user


def sample_product():
    payload = {
        "product_identifier" : "1234",
        "product_name" : "Test",
        "product_brand" : "Test",
        "product_category" : "Test",
        "product_code" : "Test",
        "product_series": "Test",
        "product_part_number": "Test",
        "business" : "Test",
    }
    product = ProductModel.objects.create(**payload)
    return product


def sample_document(product):
    payload = {
        "document_title" : "Test",
        "document_number" : "Test",
        "document_part_number" : "Test",
        "document_version": "Test",
        "document_revision": "Test",
        "document_type": "Test",
        "document_created_at": "2018-12-12",
        "document_last_edition": "2018-12-12",
        "document_last_publication": "2018-12-12",
        "document_revised_modified": "2018-12-12",
        "document_brand": "Test",
        "document_link": "Test",
        "maps_link": "Test",
        "product": product,
        "document_identifier": "Test",
    }

    document = DocumentModel.objects.create(**payload)
    return document


def sample_topic(document):
    payload = {
        "topic_title": "Test",
        "topic_breadcrumb": "Test",
        "topic_depth": 1,
        "topic_last_edition": "2018-12-12",
        "topic_link": "Test",
        "document": document,
    }
    topic = TopicModel.objects.create(**payload)
    return topic


class AnalyticsDashboardTests(TestCase):
    """Test Analytics Dashboard View"""

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.product = sample_product()
        self.document = sample_document(self.product)
        self.topic = sample_topic(self.document)

    def test_retrieve_analytics_view(self):
        """Test retrieving list of charities"""
        self.client.force_authenticate(self.user)
        response = self.client.get(DASHBOARD_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data["documents_count"]), "1")
        self.assertEqual(str(response.data["topic_count"]), "1")
        self.assertEqual(str(response.data["brand_count"]), "<QuerySet [{'document_brand': 'Test', 'brand': 1}]>")
        self.assertEqual(str(response.data["month_count"]), "<QuerySet [{'document_created_at__month': 12, 'created': 1}]>")
        self.assertEqual(str(response.data["day_of_the_week_count"]), "<QuerySet [{'weekday': 4, 'count': 1}]>")
        self.assertEqual(str(response.data["most_topics_per_document"]), "<QuerySet [{'document__document_title': 'Test', 'document__document_revision': 'Test', 'count': 1}]>")
