from django.urls import path
from .views import hospital_dashboard,list_doctors,add_doctors,edit_doctor,delete_doctor

urlpatterns = [
    path("dashboard/", hospital_dashboard, name="hospital_dashboard"),
    path("doctors/",list_doctors, name="list_doctors"),
    path("add_doctor/",add_doctors, name="add_doctor"),
    path("edit_doctor/<int:doctor_id>/",edit_doctor,name = "edit_doctor"),
    path("delete_doctor/<int:doctor_id>/",delete_doctor,name = "delete_doctor")
]
