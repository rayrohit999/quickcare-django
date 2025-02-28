from django.db import models
from django.conf import settings
# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ("Upcomming","Upcomming"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled"),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments")
    doctor_name = models.CharField(max_length=100)
    hospital_name= models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Upcoming")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.doctor_name} ({self.date} {self.time})"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medical_records")
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to="medical_records/", blank=True, null=True)

    def __str__(self):
        return f"Medical Record for {self.patient.username} on {self.date}"