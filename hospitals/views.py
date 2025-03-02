from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import HospitalProfile
from .models import Doctor,Appointment

# Create your views here.
@login_required
def hospital_dashboard(request):
    hospital=HospitalProfile.objects.get(user=request.user)
    doctors = Doctor.objects.filter(hospital=hospital)
    appointments = Appointment.objects.filter(hospital=hospital,status="Upcoming")

    context={
        "hospital":hospital,
        "doctors":doctors,
        "appointments":appointments,
    }

    return render(request,"hospitals/hospital_dashboard.html",context)

# Manage Doctors
@login_required
def list_doctors(request):
    hospital= HospitalProfile.objects.get(user=request.user)
    doctors = Doctor.objects.filter(hospital=hospital)
    
    context={
        "hospital":hospital,
        "doctors": doctors,
    }
    return render(request,'hospitals/list_doctors.html',context)

@login_required
def add_doctors(request):
    if request.method == "POST":  # Fix method check
        name = request.POST.get("name", "").strip()
        specialization = request.POST.get("specialization", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        email = request.POST.get("email", "").strip()

        # Ensure no empty fields
        if not all([name, specialization, phone_number, email]):
            messages.error(request, "All fields are required.")
            return render(request, "hospitals/add_doctor.html")

        try:
            hospital = HospitalProfile.objects.get(user=request.user)
        except HospitalProfile.DoesNotExist:
            messages.error(request, "Hospital profile not found.")
            return redirect("hospital_dashboard")  # Redirect to a relevant page

        # Create Doctor instance
        doctor = Doctor.objects.create(
            hospital=hospital,
            name=name,
            specialization=specialization,
            phone_number=phone_number,
            email=email,
        )

        messages.success(request, "Doctor added successfully!")
        return redirect("list_doctors")  # Ensure this URL name exists

    return render(request, "hospitals/add_doctor.html")

@login_required
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor,id=doctor_id)
    if request.method == "POST":
        name = request.POST.get("name").strip()
        specialization = request.POST.get("specialization").strip()
        phone_number = request.POST.get("phone_number").strip()
        email = request.POST.get("email").strip()
        
        # Validate inputs
        if not all([name, specialization, phone_number, email]):
            messages.error(request, "All fields are required.")
            return render(request, "hospitals/edit_doctor.html", {"doctor": doctor})
        
        # Update doctor details
        doctor.name = name
        doctor.specialization = specialization
        doctor.phone_number = phone_number
        doctor.email = email
        doctor.save()

        messages.success(request, "Doctor details updated successfully!")
        return redirect("list_doctors")
    
    return render(request, "hospitals/edit_doctor.html", {"doctor": doctor})

@login_required
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor,id=doctor_id)
    doctor.delete()
    return redirect("list_doctors")


