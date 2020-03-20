from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, views, status
from rest_framework.response import Response

from core.models import ProductModel
from core.permissions import IsAdminOrReadOnly
from product_search import serializers
from product_search.utils import clean_brand_list


class BrandListView(views.APIView):
    """List of Brands in dataset"""
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        brands = ProductModel.objects.order_by("product_brand").values_list("product_brand", flat=True).distinct()
        clean_brands = clean_brand_list(brands)
        return Response({"brand_list": clean_brands}, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    """Viewset for Product Model"""
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.ProductModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ["product_brand"]
    search_fields = ("product_name", "product_brand", "product_category", "product_code", "product_part_number")
    ordering_fields = "__all__"
    queryset = ProductModel.objects.order_by("product_name")

    def get_queryset(self):
        queryset = self.queryset
        return queryset
