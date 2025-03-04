from django.urls import path
from .views import patient_dashboard,book_appointment,patient_profile

urlpatterns=[
    path("dashboard/", patient_dashboard, name="patient_dashboard"),
    path("book-appointment/<int:hospital_id>",book_appointment,name="book_appointment"),
    path("profile/",patient_profile,name="patient_profile")
]
