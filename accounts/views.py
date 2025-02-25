from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm,PatientProfileForm,HospitalProfileForm
from .models import CustomUser,PatientProfile,HospitalProfile

#registeration of patient
def register_patient(request):
    if request.method=='POST':
        user_form=CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user=user_form.save(commit=False)
            user.user_type='Patient' #setting user type mannully
            user.save()
            PatientProfile.objects.create(user=user) #creating empty profile
            login(request,user)
            return redirect("complete_patient_profile") #redirecting to profile completion
    else:
        user_form=CustomUserCreationForm
    
    return render(request,'accounts/register_patient.html',{'form':user_form})

def register_hospital(request):
    if request.method=="POST":
        user_form=CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user=user_form.save(commit=False)
            user.user_type='Hospital'
            user.save()
            HospitalProfile.objects.create(user=user)
            login(request,user)
            return redirect("complete_hospital_profile")
    else:
        user_form=CustomUserCreationForm
    
    return render(request,'accounts/register_hospital.html',{'form':user_form})
    
def complete_patient_profile(request):
    if request.method=='POST':
        form= PatientProfileForm(request.POST,instance=request.user.patient_profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PatientProfileForm(instance=request.user.patient_profile)

    return render(request,'accounts/complete_patient_profile.html',{'form':form})

def complete_hospital_profile(request):
    if request.method == "POST":
        form = HospitalProfileForm(request.POST, instance=request.user.hospital_profile)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect after profile completion
    else:
        form = HospitalProfileForm(instance=request.user.hospital_profile)

    return render(request, "accounts/complete_hospital_profile.html", {"form": form})

