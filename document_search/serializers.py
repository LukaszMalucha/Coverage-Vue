from rest_framework import serializers

from core.models import DocumentModel, TopicModel
from product_search.utils import reverse_brand_name


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = "__all__"
        read_only_fields = ('id',)


class DocumentModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    # List related topics
    topics = TopicSerializer(many=True, read_only=True)

    # list clean brand string used in frontend
    clean_brand = serializers.SerializerMethodField("clean_brand_field")

    def clean_brand_field(self, obj):
        clean_brand = reverse_brand_name(obj.product.product_brand)
        return clean_brand

    class Meta:
        model = DocumentModel
        fields = "__all__"
        read_only_fields = ('id',)
        depth = 1 # To get related product details
