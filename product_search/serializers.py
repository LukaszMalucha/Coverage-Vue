from rest_framework import serializers

from core.models import ProductModel, DocumentModel


class ProductModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    class Meta:
        model = ProductModel
        fields = "__all__"
        read_only_fields = ('id',)

class DocumentModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    class Meta:
        model = DocumentModel
        fields = "__all__"
        read_only_fields = ('id',)
