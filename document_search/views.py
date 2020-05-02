from rest_framework import filters
from rest_framework import viewsets, mixins

from core.models import DocumentModel
from core.permissions import IsAdminOrReadOnly
from document_search import serializers


class DocumentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    """Model Viewset with disabled POST as we have specify the Product-Document relation"""

    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.DocumentModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("document_title", "document_number", "document_link", "document_created_at",
                     "document_last_edition", "document_brand", "document_identifier", "product__product_name",
                     "product__product_identifier", "product__product_code", "product__product_identifier")
    ordering_fields = "__all__"
    queryset = DocumentModel.objects.select_related('product').order_by("document_title", "-document_created_at")

    def get_queryset(self):
        queryset = self.queryset
        return queryset
