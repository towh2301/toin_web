from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("recruiter/", views.recruiter, name="recruiter"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:post_id>/", views.blog_detail, name="blog_detail"),
    path("keep-in-touch/", views.keep_in_touch, name="keep_in_touch"),
    path("submit-cv/", views.submit_cv, name="submit_cv"),
]
