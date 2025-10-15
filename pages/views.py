from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import get_language
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import os
from .models import (
    Hero,
    Partner,
    Post,
    Business,
    Feature,
    Product,
    CompanyProfile,
    History,
    Progress,
    Type,
    Recruiter,
    CVSubmission,
)

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from threading import Thread
import os

from .models import CVSubmission

app_name = "pages"


def index(request):
    print(settings.DEFAULT_FROM_EMAIL)

    current_language = get_language()
    heroes = Hero.objects.all()
    posts = Post.objects.all()
    businesses = Business.objects.all()
    features = Feature.objects.all()
    products = Product.objects.all()
    company_profile = (
        CompanyProfile.objects.first()
    )  # Use .first() if expecting a single profile
    history = History.objects.all()
    progresses = Progress.objects.all()
    types = Type.objects.all()
    partners = Partner.objects.all()

    context = {
        "current_language": current_language,
        "heroes": heroes,
        "posts": posts,
        "businesses": businesses,
        "features": features,
        "products": products,
        "company_profile": company_profile,
        "history": history,
        "progresses": progresses,
        "types": types,
        "partners": partners,
    }
    return render(request, "pages/index.html", context)


def recruiter(request):
    current_language = get_language()
    recruiters = Recruiter.objects.filter(is_active=True).order_by("-created_at")

    context = {
        "current_language": current_language,
        "recruiters": recruiters,
    }
    return render(request, "pages/recruiter.html", context)


def send_async_email(email_obj):
    """Send email in a separate thread (non-blocking)."""
    Thread(target=email_obj.send, daemon=True).start()


@require_POST
def submit_cv(request):
    """Handle CV submission and send email notifications."""
    try:
        # === Get form data ===
        applicant_name = request.POST.get("applicant_name")
        applicant_email = request.POST.get("applicant_email")
        applicant_phone = request.POST.get("applicant_phone", "")
        position_applied = request.POST.get("position_applied", "")
        cover_letter = request.POST.get("cover_letter", "")
        cv_file = request.FILES.get("cv_file")

        # === Validate required fields ===
        if not all([applicant_name, applicant_email, cv_file]):
            return JsonResponse(
                {
                    "success": False,
                    "message": "Please fill in all required fields and upload a CV file.",
                }
            )

        # === Validate file size and type ===
        allowed_extensions = [".pdf", ".doc", ".docx"]
        ext = os.path.splitext(cv_file.name)[1].lower()

        if cv_file.size > 5 * 1024 * 1024:  # 5MB
            return JsonResponse(
                {
                    "success": False,
                    "message": "File size must be less than 5MB.",
                }
            )

        if ext not in allowed_extensions:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Only PDF, DOC, and DOCX files are allowed.",
                }
            )

        # === Save submission ===
        cv_submission = CVSubmission.objects.create(
            applicant_name=applicant_name,
            applicant_email=applicant_email,
            applicant_phone=applicant_phone,
            position_applied=position_applied,
            cover_letter=cover_letter,
            cv_file=cv_file,
        )

        # === Prepare email to HR ===
        subject_hr = f"New CV Submission - {applicant_name}"
        message_hr = f"""
New CV submission received:

Name: {applicant_name}
Email: {applicant_email}
Phone: {applicant_phone or 'Not provided'}
Position: {position_applied or 'General Application'}

Cover Letter:
{cover_letter or 'No cover letter provided'}

Please check the attached CV file.
"""

        email_hr = EmailMessage(
            subject=subject_hr,
            body=message_hr,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["huy.buihoang.cit20@eiu.edu.vn"],
            reply_to=[applicant_email],
        )
        email_hr.attach_file(cv_submission.cv_file.path)

        # === Prepare confirmation email to applicant ===
        subject_applicant = "CV Submission Confirmation - TOIN Vietnam"
        message_applicant = f"""
Dear {applicant_name},

Thank you for your interest in joining TOIN Vietnam!

We have received your CV submission for the position: {position_applied or 'General Application'}.

Our HR team will review your application and contact you if there’s a suitable match.

Best regards,
TOIN Vietnam HR Team
"""

        # === Send both emails asynchronously ===
        try:
            send_async_email(email_hr)
            Thread(
                target=send_mail,
                args=(
                    subject_applicant,
                    message_applicant,
                    settings.DEFAULT_FROM_EMAIL,
                    [applicant_email],
                ),
                kwargs={"fail_silently": False},
                daemon=True,
            ).start()

            return JsonResponse(
                {
                    "success": True,
                    "message": "Your CV has been submitted successfully! We will contact you soon.",
                }
            )

        except Exception as e:
            # Email failed — still save record
            cv_submission.notes = f"Email sending failed: {str(e)}"
            cv_submission.save()

            return JsonResponse(
                {
                    "success": True,
                    "message": "Your CV was submitted, but we couldn’t send confirmation email right now.",
                }
            )

    except Exception as e:
        return JsonResponse(
            {
                "success": False,
                "message": f"An unexpected error occurred: {str(e)}",
            }
        )
