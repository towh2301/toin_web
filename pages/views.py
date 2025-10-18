import os
import logging
from threading import Thread

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import get_language
from django.views.decorators.http import require_POST

from .models import CVSubmission
from .models import (
    CompanyProfile,
    Progress,
    Type,
    Post,
    Hero,
    Product,
    History,
    Feature,
    Partner,
    Recruiter,
    Business,
)

app_name = "pages"

logger = logging.getLogger(__name__)


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
    company_profile = (
        CompanyProfile.objects.first()
    )  # Use .first() if expecting a single profile

    context = {
        "company_profile": company_profile,
        "current_language": current_language,
        "recruiters": recruiters,
    }
    return render(request, "pages/recruiter.html", context)


def blog_list(request):
    """Simple blog listing using Post model."""
    posts = Post.objects.filter(is_published=True).order_by("-publish_date")
    return render(request, "pages/blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    post = Post.objects.filter(id=post_id, is_published=True).first()
    company_profile = CompanyProfile.objects.first()
    recent_posts = (
        Post.objects.filter(is_published=True)
        .exclude(id=post_id)
        .order_by("-publish_date")[:5]
    )
    if not post:
        from django.http import Http404

        raise Http404("Post not found")
    return render(
        request,
        "pages/blog_detail.html",
        {
            "post": post,
            "recent_posts": recent_posts,
            "company_profile": company_profile,
        },
    )


@require_POST
def keep_in_touch(request):
    """Handle Keep-in-touch contact submissions from the contact form.

    Expects: name, email, subject, message
    Sends an email to site contact and a confirmation to the sender.
    Returns JSON.
    """
    try:
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not all([name, email, subject, message]):
            return JsonResponse(
                {"success": False, "message": "Please fill in all required fields."}
            )

        # Compose email to site contact
        from django.conf import settings

        hr_subject = f"Keep in touch: {subject} - from {name}"
        hr_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        email_hr = EmailMessage(
            subject=hr_subject,
            body=hr_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[email],
        )

        # Send asynchronously
        send_async_email(email_hr)

        # Send confirmation to the sender
        conf_subject = "Thanks for contacting TOIN Vietnam"
        conf_message = f"Dear {name},\n\nThank you for reaching out. We received your message and will reply as soon as possible.\n\nBest regards,\nTOIN Vietnam"
        Thread(
            target=send_mail,
            args=(conf_subject, conf_message, settings.DEFAULT_FROM_EMAIL, [email]),
            kwargs={"fail_silently": True},
            daemon=True,
        ).start()

        return JsonResponse(
            {"success": True, "message": "Thank you — your message has been sent."}
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"An error occurred: {str(e)}"}
        )


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
            to=[settings.DEFAULT_TO_EMAIL],
            reply_to=[applicant_email],
        )
        email_hr.attach_file(cv_submission.cv_file.path)

        # === Prepare confirmation email to applicant ===
        subject_applicant = "CV Submission Confirmation - TOIN Vietnam"
        message_applicant = f"""
Dear {applicant_name},

Thank you for your interest in joining TOIN Vietnam!

We have received your CV submission for the position: {position_applied or 'General Application'}.

Our HR team will review your application and contact you if there's a suitable match.

Best regards,
TOIN Vietnam HR Team
"""

        # === Send both emails (NOT as daemon threads) ===
        try:
            # Send HR email
            email_hr.send(fail_silently=False)
            logger.info(f"HR email sent for submission {cv_submission.id}")

            # Send applicant confirmation email
            send_mail(
                subject_applicant,
                message_applicant,
                settings.DEFAULT_FROM_EMAIL,
                [applicant_email],
                fail_silently=False,
            )
            logger.info(f"Confirmation email sent to {applicant_email}")

            return JsonResponse(
                {
                    "success": True,
                    "message": "Your CV has been submitted successfully! We will contact you soon.",
                }
            )

        except Exception as e:
            # Email failed — log and save error
            error_msg = f"Email sending failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            cv_submission.notes = error_msg
            cv_submission.save()

            return JsonResponse(
                {
                    "success": True,
                    "message": "Your CV was submitted, but we couldn't send confirmation email right now.",
                }
            )

    except Exception as e:
        logger.error(f"CV submission error: {str(e)}", exc_info=True)
        return JsonResponse(
            {
                "success": False,
                "message": f"An unexpected error occurred: {str(e)}",
            }
        )


# Error Handler Views
# These views provide styled error pages with header and footer
def page_not_found(request, exception=None):
    """Handle 404 Page Not Found errors.

    Renders a branded 404 error page with header and footer.
    """
    return render(request, "404.html", status=404)


def server_error(request):
    """Handle 500 Server Error.

    Renders a branded 500 error page with header and footer.
    """
    return render(request, "500.html", status=500)
