from django.urls import path, include
from rest_framework.routers import DefaultRouter

from document_search import views

app_name = "documents"

router = DefaultRouter()

router.register("documents", views.DocumentViewSet, basename="documents")

urlpatterns = [
    path("", include(router.urls)),
]
