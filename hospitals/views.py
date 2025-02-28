from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import HospitalProfile
from .models import Doctor,Appointment

# Create your views here.
@login_required
def hospital_dashboard(request):
    hospital=HospitalProfile.objects.get(user=request.user)
    doctors = Doctor.objects.filter(hospital=hospital)
    appointments = Appointment.objects.filter(hospital=hospital)

    context={
        "hospital":hospital,
        "doctors":doctors,
        "appointments":appointments,
    }

    return render(request,"hospitals/hospital_dashboard.html",context)