from django.urls import path

from db_manager import views

app_name = "db_manager"

urlpatterns = [
    path("db-manager", views.db_manager, name="db-manager"),
    path("bulk-products", views.bulk_products, name="bulk-products"),
    path("bulk-documents", views.bulk_documents, name="bulk-documents"),
    path("bulk-topics", views.bulk_topics, name="bulk-topics"),
    path("products-upload", views.products_upload, name="products-upload"),
    path("documents-upload", views.documents_upload, name="documents-upload"),
    path("topics-upload", views.topics_upload, name="topics-upload"),
    path("download-queryset", views.download_queryset, name="download-queryset")
]