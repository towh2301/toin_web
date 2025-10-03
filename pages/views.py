from django.shortcuts import render
from .models import Introduction

def introduction(request):
    intro = Introduction.objects.first()  # only one intro
    return render(request, "base.html", {"intro": intro})
