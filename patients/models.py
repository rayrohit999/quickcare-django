from django.db import models
from django.conf import settings
# Create your models here.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medical_records")
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to="medical_records/", blank=True, null=True)

    def __str__(self):
        return f"Medical Record for {self.patient.username} on {self.date}"