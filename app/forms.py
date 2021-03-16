from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, CovidSymptom
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email", "image")

class CovidForm(ModelForm):
    class Meta:
        model = CovidSymptom
        fields = '__all__'