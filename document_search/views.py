from rest_framework import viewsets, status, filters, authentication, permissions, views, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from document_search import serializers

from core.models import ProductModel, DocumentModel
from core.permissions import IsAdminOrReadOnly



class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.DocumentModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("document_title", "document_number","product__product_name")
    ordering_fields = "__all__"
    queryset = DocumentModel.objects.order_by("document_title")

    def get_queryset(self):
        queryset = self.queryset
        return queryset


