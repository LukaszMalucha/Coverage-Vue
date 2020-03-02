from rest_framework import viewsets, filters
from document_search import serializers
from core.models import DocumentModel
from core.permissions import IsAdminOrReadOnly




class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.DocumentModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("document_title", "document_number",)
    ordering_fields = "__all__"
    queryset = DocumentModel.objects.filter(document_category="document")

    def get_queryset(self):
        queryset = self.queryset
        return queryset
