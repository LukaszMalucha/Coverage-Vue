from django.urls import path, include
from rest_framework.routers import DefaultRouter

from brand_search import views

app_name = "brands"

router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('brand-list/', views.BrandListView.as_view(), name="brand-list"),
    path("<str:brand>/",  views.BrandAPIView.as_view(), name="brand")
]