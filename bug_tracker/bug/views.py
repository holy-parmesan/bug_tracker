from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, BugForm
from .models import Bug


def home(request):
    return render(request, "bug/home.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account was created successfully"
            )
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "bug/register.html", {"form": form})


@login_required()
def profile(request):
    return render(request, "bug/profile.html")
