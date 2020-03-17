from django.urls import path, include

from analytics import views

app_name = "analytics"




urlpatterns = [
    path("dashboard",  views.AnalyticsDashboardView.as_view(), name="dashboard"),
]