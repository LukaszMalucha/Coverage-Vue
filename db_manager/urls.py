from django.urls import path

from db_manager import views

app_name = "db_manager"

urlpatterns = [
    path("db-manager", views.db_manager, name="db-manager"),
    path("bulk-products-upload", views.bulk_products_upload, name="bulk-products-upload"),
    path("bulk-documents-upload", views.bulk_documents_upload, name="bulk-documents-upload"),
    path("bulk-topics-upload", views.bulk_topics_upload, name="bulk-topics-upload"),
    path("products-upload", views.products_upload, name="products-upload"),
    path("documents-upload", views.documents_upload, name="documents-upload"),
    path("topics-upload", views.topics_upload, name="topics-upload")
]