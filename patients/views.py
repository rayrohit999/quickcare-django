from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MedicalRecord  # Assuming these models exist
from hospitals.models import Appointment,Doctor
from accounts.models import HospitalProfile,PatientProfile
from datetime import date
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

#book appointment
@login_required
def book_appointment(request,hospital_id):
    hospital = HospitalProfile.objects.get(id=hospital_id)
    doctors = Doctor.objects.filter(hospital=hospital)
    if request.method == "POST":
        patient = request.user
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        doctor = get_object_or_404(Doctor, id=doctor_id)  


        appointment = Appointment.objects.create(hospital=hospital,doctor=doctor,patient=patient,date=date,time=time)
        return redirect("patient_dashboard")


    return render(request,"patients/book_appointment.html",{"doctors":doctors})

@login_required
def patient_profile(request):
    patient = PatientProfile.objects.get(user=request.user)
    def calculate_age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    patient_age = calculate_age(patient.date_of_birth) if patient.date_of_birth else "N/A"
    return render(request,"patients/patient_profile.html",{"patient":patient,"age":patient_age})