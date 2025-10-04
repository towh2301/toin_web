from django.shortcuts import render, redirect
from django.urls import reverse

from pages.models import Hero
from django.utils.translation import gettext as _, activate


def index(request):
    return render(request, "base.html")


def set_language(request):
    language = request.POST.get("language")
    if language:
        activate(language)
        request.session['django_language'] = language
    return redirect(reverse(''))
