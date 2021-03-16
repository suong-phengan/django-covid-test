from django.urls import path, include
from .views import index, register, hospital_details, symptom_analysis

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("details/", hospital_details, name="hospital_details"),
    path("symptom_analysis", symptom_analysis, name="symptom_analysis")
]