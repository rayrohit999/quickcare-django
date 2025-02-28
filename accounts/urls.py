from django.urls import path
from .views import (
    register_patient, register_hospital, 
    complete_patient_profile, complete_hospital_profile, custom_login
)
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path("register/patient/", register_patient, name="register_patient"),
    path("register/hospital/", register_hospital, name="register_hospital"),
    path("profile/patient/", complete_patient_profile, name="complete_patient_profile"),
    path("profile/hospital/", complete_hospital_profile, name="complete_hospital_profile"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("login/", custom_login, name="login"),
]
