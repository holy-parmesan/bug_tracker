import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, BugForm
from .models import bug


def home(request):
    todo_list = bug.objects.all()
    form = BugForm()
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("/")
    page = {
        "forms": form,
        "list": todo_list,
        "title": "TODO LIST",
    }
    return render(request, "bug/home.html", page)


def add(request):
    obj = bug()
    obj.title = request.POST["title"]
    obj.date = request.POST["date"]
    obj.body = request.POST["body"]
    obj.save()
    mydict = {"todo_list": bug.objects.all()}
    messages.info(request, "item added!!!")
    return render(request, "bug/home.html", context=mydict)


def delete(request, i):
    item = bug.objects.get(id=i)
    # item = request.POST[item]
    item.delete()
    mydict = {"todo_list": bug.objects.all()}
    messages.info(request, "item removed!!!")
    return render(request, "bug/home.html", context=mydict)


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
