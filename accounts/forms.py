from .models import CustomUser,PatientProfile,HospitalProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model=PatientProfile
        fields=['date_of_birth','phone_number','gender','address','blood_group','medical_history','emergency_contact']

class HospitalProfileForm(forms.ModelForm):
    class Meta:
        model=HospitalProfile
        fields=['hospital_name','registration_number','phone_number','address','city','state','zip_code','specialization','emergency_services']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))