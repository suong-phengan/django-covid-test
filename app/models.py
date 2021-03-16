from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='static/images/', blank = True)

class CovidSymptom(models.Model):
    user_id = models.IntegerField(null=True)
    fever = models.BooleanField(default=False)
    dry_cough = models.BooleanField(default=False)
    tiredness = models.BooleanField(default=False)
    diarrihoea = models.BooleanField(default=False)
    difficulty_breathing = models.BooleanField(default=False)
    shortness_of_breath = models.BooleanField(default=False)
    chest_pain = models.BooleanField(default=False)
    chest_pressure = models.BooleanField(default=False)
    loss_of_speech = models.BooleanField(default=False)
    loss_of_movement= models.BooleanField(default=False)

