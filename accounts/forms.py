from .models import CustomUser,PatientProfile,HospitalProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email',
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter  username',
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
        })
    )
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']

class PatientProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})
    )

    class Meta:
        model = PatientProfile
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'address',
            'blood_group', 'medical_history', 'emergency_contact'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
            ]),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'rows': 2}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blood group'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any medical history', 'rows': 3}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter emergency contact'}),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name = self.cleaned_data['last_name']
        if commit:
            profile.user.save()
            profile.save()
        return profile


class HospitalProfileForm(forms.ModelForm):
    class Meta:
        model = HospitalProfile
        fields = [
            'hospital_name', 'registration_number', 'phone_number', 'address', 
            'city', 'state', 'zip_code', 'specialization', 'emergency_services'
        ]
        widgets = {
            'hospital_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hospital name'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter registration number'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter hospital address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zip code'}),
            'specialization': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter hospital specialization', 'rows': 2}),
            'emergency_services': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )