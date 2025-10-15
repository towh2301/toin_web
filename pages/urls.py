from django.urls import path, include
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("recruiter/", views.recruiter, name="recruiter"),
    path("submit-cv/", views.submit_cv, name="submit_cv"),
]
