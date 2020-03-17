from rest_framework import viewsets, status, filters, authentication, permissions, views, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from document_search import serializers
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractWeekDay

from core.models import ProductModel, DocumentModel, TopicModel
from core.permissions import IsAdminOrReadOnly


class AnalyticsDashboardView(views.APIView):

    def get(self, request):
        document_count = DocumentModel.objects.count()
        topic_count = TopicModel.objects.count()
        brand_count = DocumentModel.objects.values("document_brand").annotate(brand=Count('document_brand'))
        month_count = DocumentModel.objects.filter(document_created_at__range=["2014-01-01", "2019-12-31"]).values(
            "document_created_at__month").annotate(created=Count('document_created_at__month'))
        day_of_the_week_count = DocumentModel.objects.filter(document_created_at__range=["2014-01-01", "2019-12-31"]) \
            .annotate(weekday=ExtractWeekDay('document_created_at')) \
            .values('weekday') \
            .annotate(count=Count('id')) \
            .values('weekday', 'count')  # FIRST DAY = SUNDAY

        most_topics_per_document = TopicModel.objects.values("document").annotate(count=Count('document')).values('document__document_title', 'document__document_revision','count').order_by('-count')[:10]



        return Response({"documents_count": document_count, "topic_count": topic_count, "brand_count": brand_count,
                         "month_count": month_count, "day_of_the_week_count": day_of_the_week_count, "most_topics_per_document": most_topics_per_document})
