from django.urls import path
from .views import hospital_dashboard,list_doctors,add_doctors,edit_doctor,delete_doctor,list_hospitals,hospital_profile

urlpatterns = [
    path("dashboard/", hospital_dashboard, name="hospital_dashboard"),
    path("doctors/",list_doctors, name="list_doctors"),
    path("add-doctor/",add_doctors, name="add_doctor"),
    path("edit-doctor/<int:doctor_id>/",edit_doctor,name = "edit_doctor"),
    path("delete-doctor/<int:doctor_id>/",delete_doctor,name = "delete_doctor"),
    path("hospitals-list",list_hospitals,name="list_hospital"),
    path("profile/",hospital_profile,name="hospital_profile")
]
