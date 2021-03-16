from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm, CovidForm
from .models import CovidSymptom
from django.forms.models import model_to_dict


# Create your views here.


def index(request):
    symptoms = CovidSymptom.objects.all().filter(user_id = request.user.id).order_by("id").reverse()
    if symptoms:
        symptoms = symptoms[0]
        symptoms = model_to_dict(symptoms)
        symptoms = list(symptoms.values())
        x = symptoms.count(True)
        y = symptoms.count(False)
        context = {"x":x, "y":y}
        print(context)
    else:
        context = {}
    return render(request, "index.html", context)


def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        try:
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
        except:
            return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )

def hospital_details(request):
    if request.user.is_authenticated:
        return render(request, "hospital_details.html")
    else:
        return redirect(reverse("login"))

def symptom_analysis(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "symptom_analysis.html", {"form": CovidForm})
        else:
            return redirect(reverse("login"))
    elif request.method == "POST":
        post = request.POST.copy()
        post['user_id'] = request.user.id
        request.POST = post
        form = CovidForm(post, request.FILES)
        if form .is_valid():
            form.save()
            return redirect(reverse("index"))
