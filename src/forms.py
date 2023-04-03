from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



class employee_form(forms.Form):
    username = forms.CharField(label='Patient Username (enter username without space)', max_length=50)
    department = forms.CharField(label='Patient Department', max_length=100)
    phone = forms.CharField(label='Patient Phone', max_length=20)
    d_date = forms.DateField(label="Select Appointment Date",required=True, widget=NumberInput(attrs={'type':'date'}))
    start_time = forms.CharField(label='Appointment Start Time') 
    end_time = forms.CharField(label='Appointment End Time')
    doctor_name = forms.CharField(label="Doctor's Name")
class update_employee_form(forms.ModelForm):
    class Meta:
        model   = patient
        exclude = ('role_admin_id' , 'user' , 'otp')

class profileUpdate(forms.ModelForm):
    class Meta:
        model   = patient_profile
        fields = (
            "name",
            "email",
            "about",
            "image"
        )
        


class ShiftForm(forms.ModelForm):
    d_date = forms.DateField(label="Select Appointment End Date",required=True, widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = patient_appointment
        fields = (
            "d_date",
            "start_time",
            "end_time",
            "doctor_name",
        )

# class attendance_form(forms.ModelForm):
#     date = forms.DateField(label="Select Date",required=True, widget=NumberInput(attrs={'type':'date'}))   
#     class Meta:
#         model = attendance
#         exclude = ('employee_id',)


# class salary_form(forms.ModelForm):
#     date = forms.DateField(label="Select Date",required=True, widget=NumberInput(attrs={'type':'date'}))   
#     class Meta:
#         model = salary
#         exclude = ('employee_id',)


# class project_tracking_form(forms.ModelForm):
#     class Meta:
#         model = project_tracking
#         exclude = ('employee_id',)
