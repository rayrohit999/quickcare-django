from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission


# Create your models here.
class CustomUser(AbstractUser):
    user_type=models.CharField(max_length=50)

    # Avoid conflicts with Django's default User model
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return f"{self.username}-{self.user_type}"

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="patient_profile")
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)  # Any past medical records
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Patient: {self.user.username}"
    
class HospitalProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="hospital_profile")
    hospital_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    specialization = models.TextField(blank=True, null=True)  # Special services provided
    emergency_services = models.BooleanField(default=False)  # True if hospital has emergency care

    def __str__(self):
        return f"Hospital: {self.hospital_name}"