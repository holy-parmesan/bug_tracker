import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, BugForm
from .models import bug


def home(request):
    todo_list = ["foo", "bar", "bah"]
    todo_list = bug.objects.all()
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("/")
    form = BugForm()
    page = {
        "forms": form,
        "list": todo_list,
        "title": "TODO LIST",
    }

    return render(request, "bug/home.html", page)


def add(request):
    obj = bug()
    # obj.id = request.POST["id"]
    obj.title = request.POST["title"]
    obj.date = request.POST["date"]
    obj.body = request.POST["body"]
    obj.save()
    mydict = {"todo_list": bug.objects.all()}
    messages.info(request, "item added!!!")
    # return redirect("/", context=mydict)
    return render(request, "bug/home.html", context=mydict)
    # if request.method == "POST":
    #     if "addBug" in request.POST:
    #         form = BugForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #         # title = request.POST["title"]
    #         # id = request.POST["id"]
    #         # date = str(request.POST["date"])
    #         # body = request.POST["body"]
    #         # single_bug = bug(title=title, id=id, date=date, body=body)
    #         # single_bug.save()
    #         return redirect("/")
    # # item = bug.objects.get()
    # # item.save()


def remove(request, pk):
    item = bug.objects.get(id=pk)
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
