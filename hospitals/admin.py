from django.contrib import admin

# Register your models here.
from .models import Doctor,Appointment


admin.site.register(Doctor)
admin.site.register(Appointment)    