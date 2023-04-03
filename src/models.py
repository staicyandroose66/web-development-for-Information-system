from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES=(
    ('Active','Active'),
    ('Inactive','Inactive'),
)

attendance_status=(
    ('Present','Present'),
    ('Absent','Absent'),
)

class role_admin(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)


class patient(models.Model):
    role_admin_id   = models.ForeignKey(role_admin, on_delete=models.CASCADE)
    user            = models.ForeignKey(User,       on_delete=models.CASCADE)
    department         = models.CharField(max_length=50)
    status          = models.CharField(max_length=50 , choices=STATUS_CHOICES , default='Active')
    phone           = models.CharField(max_length=20)
    otp             = models.IntegerField(default=0)
    created_at      =  models.DateTimeField(auto_now_add=True)
    updated_at      =  models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username



class patient_profile(models.Model):
    employee_id     = models.ForeignKey(patient , on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    phone           = models.CharField(max_length=20 , null=True , blank=True)
    email           = models.EmailField(max_length=50 , null=True , blank=True)
    about           = models.TextField(null=True , blank=True)
    image           = models.ImageField(default="default.jpeg", upload_to='images/')


class patient_appointment(models.Model):
    role_admin_id       = models.ForeignKey(role_admin, on_delete=models.CASCADE)
    employee_id         = models.ForeignKey(patient, on_delete=models.CASCADE)       
    d_date              = models.DateField()
    start_time          = models.CharField(max_length=10)
    end_time            = models.CharField(max_length=10)
    doctor_name         = models.CharField(max_length=20)
    staus               = models.BooleanField(default=False)


project_status = (
    ('inprogress', 'In Progress'),
    ('completed', 'Completed'),
    ('pending', 'Pending'),)

# uses your employee profile details, compliance rules, and staffing budgets to help you plan shifts, calculate labour costs and create and send rosters to employees.   