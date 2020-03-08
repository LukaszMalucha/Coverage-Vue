from rest_framework import serializers
from random import randrange
from core.models import ProductModel, DocumentModel



class ProductModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    image = serializers.SerializerMethodField("img_field")

# GENERATED FOR TESTING BEFORE I GET REAL ONES
    def img_field(self, obj):
        return randrange(9) + 1

    class Meta:
        model = ProductModel
        fields = "__all__"
        read_only_fields = ('id',)

