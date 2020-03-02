from django.conf import settings
from rest_framework import viewsets, status, filters, authentication, permissions, views, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from product_search import serializers
from product_search.utils import clean_brand_list, get_brand_name
from core.models import ProductModel, DocumentModel
from core.permissions import IsAdminOrReadOnly


class BrandAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductModelSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("product_name", "product_code", "product_series", "product_part_number")
    
    def get_queryset(self):
        kwarg_brand = self.kwargs.get("brand")
        brand = get_brand_name(kwarg_brand)
        return ProductModel.objects.filter(product_brand=brand).order_by("product_name")


class BrandListView(views.APIView):
    """List of Brands in dataset"""
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        brands = ProductModel.objects.order_by("product_brand").values_list("product_brand", flat=True).distinct()
        clean_brands = clean_brand_list(brands)
        return Response({"brand_list": clean_brands})
