from django.contrib import admin
from .models import CustomUser,PatientProfile,HospitalProfile
# Register your models here.
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'phone_number', 'blood_group']

class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = ['hospital_name', 'registration_number', 'phone_number', 'city', 'state']

admin.site.register(CustomUser)
admin.site.register(PatientProfile, PatientProfileAdmin)
admin.site.register(HospitalProfile, HospitalProfileAdmin)