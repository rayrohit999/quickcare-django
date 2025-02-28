from django.urls import path
from .views import hospital_dashboard

urlpatterns = [
    path("dashboard/", hospital_dashboard, name="hospital_dashboard")
]
