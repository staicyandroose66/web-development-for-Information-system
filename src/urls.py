from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('sign-in/',signin , name='sign-in'),
    path('add-patient/',add_patient , name='add-patient'),
    path('update-employee/<int:pk>/',update_employee , name='update-employee'),
    path('logout/',logout , name='logout'),
    path('shift-management' , shift_management , name="shift-management"),
    path('add-shift/<int:pk>/' , add_shift , name="add-shift") ,
    path('update-shift/<int:pk>/' , update_shift , name="update-shift") ,
    # Employee
    path('signin-emp/' , signin_emp , name="signin-emp"),
    path('verify-otp' , verify_otp , name="verify-otp") ,
    path('profile' , profile , name="profile"),
    path('profile-update' , profile_update , name="profile-update"),
]
