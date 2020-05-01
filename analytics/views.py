from django.db.models import Count
from django.db.models.functions import ExtractWeekDay
from rest_framework import views, status
from rest_framework.response import Response
from core.permissions import IsAdminOrReadOnly
from core.models import DocumentModel, TopicModel, ProductModel


class AnalyticsDashboardView(views.APIView):
    """View that sends the data to Analytic Dashboard charts"""

    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        document_count = DocumentModel.objects.count()
        topic_count = TopicModel.objects.count()
        product_count = ProductModel.objects.count()

        brand_count = DocumentModel.objects.values("document_brand").annotate(count=Count('document_brand')).order_by('-count')[:15]
        brand_count_dict = {}
        for element in brand_count:
            brand_count_dict[element['document_brand']] = element['count']

        month_count = DocumentModel.objects.filter(document_created_at__range=["2014-01-01", "2019-12-31"]).values(
            "document_created_at__month").annotate(created=Count('document_created_at__month'))
        month_count_dict = {}
        for element in month_count:
            month_count_dict[element['document_created_at__month']] = element['created']

        day_of_the_week_count = DocumentModel.objects.filter(document_created_at__range=["2014-01-01", "2019-12-31"]) \
            .annotate(weekday=ExtractWeekDay('document_created_at')) \
            .values('weekday') \
            .annotate(count=Count('id')) \
            .values('weekday', 'count')  # FIRST DAY OF THE WEEK = SUNDAY
        day_of_the_week_count_dict = {}
        for element in day_of_the_week_count:
            day_of_the_week_count_dict[element['weekday']] = element['count']

        most_topics_per_document = TopicModel.objects.values("document").annotate(count=Count('document')).values(
            'document__document_title', 'document__document_revision', 'count').order_by('-count')[:5]
        most_topics_per_document_dict = {}
        for element in most_topics_per_document:
            most_topics_per_document_dict[element['document__document_title']] = element['count']

        document_type_count = DocumentModel.objects.values("document_type").annotate(count=Count('document_type')).order_by('-count')[:10]
        document_type_count_dict = {}
        for element in document_type_count:
            document_type_count_dict[element['document_type']] = element['count']

        return Response({"document_count": document_count, "topic_count": topic_count, "product_count": product_count,
                         "brand_count_dict": brand_count_dict, "month_count_dict": month_count_dict,
                         "day_of_the_week_count_dict": day_of_the_week_count_dict,
                         "most_topics_per_document_dict": most_topics_per_document_dict,
                         "document_type_count_dict": document_type_count_dict}, status=status.HTTP_200_OK)
