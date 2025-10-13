from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from converter import views

app_name = "converter"

urlpatterns = [
    path("", views.index, name="converter"),
    path("convert/", views.convert_pdf, name="convert_pdf"),
]
