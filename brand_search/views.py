import json
import os

from django.conf import settings
from rest_framework import viewsets, status, filters, authentication, permissions, views, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from brand_search import serializers
from brand_search.utils import clean_brand_list, get_brand_name
from core.models import DocumentModel
from core.permissions import IsAdminOrReadOnly




class BrandAPIView(generics.ListAPIView):

    serializer_class = serializers.DocumentModelSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        kwarg_brand = self.kwargs.get("brand")
        brand = get_brand_name(kwarg_brand)
        return DocumentModel.objects.filter(product_brand=brand).order_by("document_title")


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.DocumentModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("document_title", "topic_title", "product_name", "product_code")
    ordering_fields = "__all__"
    queryset = DocumentModel.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        brand = self.request.query_params.get('product_brand', None)
        if brand is None:
            queryset = DocumentModel.objects.all()
        return queryset


class BrandListView(views.APIView):
    """List of Brands in dataset"""
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        brands = DocumentModel.objects.order_by("product_brand").values_list("product_brand", flat=True).distinct()
        clean_brands = clean_brand_list(brands)
        return Response({"brand_list": clean_brands})