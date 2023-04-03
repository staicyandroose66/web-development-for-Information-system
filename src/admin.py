from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(role_admin)
admin.site.register(patient)
admin.site.register(patient_profile)
admin.site.register(patient_appointment)