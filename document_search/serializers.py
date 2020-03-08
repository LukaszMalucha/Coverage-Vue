from rest_framework import serializers

from core.models import DocumentModel, ProductModel
from product_search.utils import reverse_brand_name


class DocumentModelSerializer(serializers.ModelSerializer):
    """Serializer for Document Model"""

    topics = serializers.SerializerMethodField("topics_field")
    clean_brand = serializers.SerializerMethodField("clean_brand_field")

    def topics_field(self, obj):

        if obj.document_number != "Not Specified":
            topics = DocumentModel.objects.filter(document_number=obj.document_number).values()
            # document_last_edition, document_title, id, product_id, document_link
            remove_set = {"document_revision", "document_version",
                          "document_type", "document_lang", "document_created_at",
                          "document_last_publication", "document_revised_modified",
                          "maps_link", "uploaded"}
            for dict in topics:
                [dict.pop(key) for key in remove_set]
        else:
            topics = []
        return topics



    def clean_brand_field(self, obj):
        clean_brand = reverse_brand_name(obj.product.product_brand)
        return clean_brand

    class Meta:
        model = DocumentModel
        fields = "__all__"
        read_only_fields = ('id',)
        depth = 1
