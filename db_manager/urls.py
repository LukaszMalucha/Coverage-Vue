from django.urls import path

from db_manager import views

app_name = "db_manager"

urlpatterns = [
    path("db-manager", views.db_manager, name="db-manager"),
    path("products-upload", views.products_upload, name="products-upload"),
    path("documents-upload", views.documents_upload, name="documents-upload"),
]