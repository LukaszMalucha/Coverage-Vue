from rest_framework import serializers

from core.models import DocumentModel


class DocumentModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    class Meta:
        model = DocumentModel
        fields = "__all__"
        read_only_fields = ('id',)

