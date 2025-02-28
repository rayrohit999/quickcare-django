from django.db import models
from accounts.models import HospitalProfile
from django.conf import settings

# Create your models here.
class Doctor(models.Model):
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=40)
    phone_number=models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.name}- {self.specialization}"
    
class Appointment(models.Model):
    hospital= models.ForeignKey(HospitalProfile,on_delete=models.CASCADE,related_name="appointments")
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hospital_appointment")
    docotor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="appointments")
    date = models.DateField
    time = models.TimeField
    status= models.CharField(max_length=20,choices=[
        ("Scheduled","Scheduled"),
        ("Completed","Cancled"),
        ("Cancled","Cancled")
    ])

    def __str__(self):
        return f"{self.patient.username}-{self.docotor.name} ({self.date} {self.time})"