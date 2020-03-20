from random import randrange

from rest_framework import serializers

from core.models import ProductModel
from product_search.utils import reverse_brand_name


class ProductModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    image = serializers.SerializerMethodField("img_field")
    clean_brand = serializers.SerializerMethodField("clean_brand_field")

    # GENERATED IMAGE BEFORE I GET REAL ONES
    def img_field(self, obj):
        return randrange(9) + 1

    def clean_brand_field(self, obj):
        clean_brand = reverse_brand_name(obj.product_brand)
        return clean_brand

    class Meta:
        model = ProductModel
        fields = "__all__"
        read_only_fields = ('id',)
