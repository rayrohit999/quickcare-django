from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MedicalRecord  # Assuming these models exist
from hospitals.models import Appointment
@login_required
def patient_dashboard(request):
    upcoming_appointments = Appointment.objects.filter(patient=request.user, status="Upcoming")
    past_appointments = Appointment.objects.filter(patient=request.user, status="Completed")
    medical_records = MedicalRecord.objects.filter(patient=request.user)

    context = {
        'upcoming_appointments': upcoming_appointments,
        'past_appointments': past_appointments,
        'medical_records': medical_records,
    }
    return render(request, "patients/patients_dashboard.html", context)