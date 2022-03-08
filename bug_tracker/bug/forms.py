from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from bug_tracker.bug.models import Bug


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = "__all__"
