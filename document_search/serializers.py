from rest_framework import serializers

from core.models import DocumentModel, ProductModel, TopicModel
from product_search.utils import reverse_brand_name



class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = "__all__"
        read_only_fields = ('id',)


class DocumentModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    topic = TopicSerializer(many=True, read_only=True)
    clean_brand = serializers.SerializerMethodField("clean_brand_field")

    def clean_brand_field(self, obj):
        clean_brand = reverse_brand_name(obj.product.product_brand)
        return clean_brand

    class Meta:
        model = DocumentModel
        fields = "__all__"
        read_only_fields = ('id',)
        depth = 1