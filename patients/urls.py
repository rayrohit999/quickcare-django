from django.urls import path
from .views import patient_dashboard,book_appointment

urlpatterns=[
    path("dashboard/", patient_dashboard, name="patient_dashboard"),
    path("book-appointment/<int:hospital_id>",book_appointment,name="book_appointment")
]
