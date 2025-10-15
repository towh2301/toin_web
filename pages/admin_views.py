from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils import timezone
from datetime import timedelta
import json
import csv
from io import StringIO
from .models import CVSubmission


@staff_member_required
@require_POST
def mark_processed(request, submission_id):
    """Mark a CV submission as processed"""
    try:
        submission = get_object_or_404(CVSubmission, id=submission_id)
        submission.is_processed = True
        submission.save()

        return JsonResponse(
            {"success": True, "message": "Submission marked as processed"}
        )
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"})


@staff_member_required
@require_POST
def mark_pending(request, submission_id):
    """Mark a CV submission as pending"""
    try:
        submission = get_object_or_404(CVSubmission, id=submission_id)
        submission.is_processed = False
        submission.save()

        return JsonResponse(
            {"success": True, "message": "Submission marked as pending"}
        )
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"})


@staff_member_required
@require_POST
def update_notes(request, submission_id):
    """Update internal notes for a submission"""
    try:
        submission = get_object_or_404(CVSubmission, id=submission_id)
        data = json.loads(request.body)
        submission.notes = data.get("notes", "")
        submission.save()

        return JsonResponse({"success": True, "message": "Notes updated successfully"})
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"})


@staff_member_required
@require_POST
def bulk_action(request):
    """Handle bulk actions on CV submissions"""
    try:
        data = json.loads(request.body)
        action = data.get("action")
        ids = data.get("ids", [])

        if not ids:
            return JsonResponse(
                {"success": False, "message": "No submissions selected"}
            )

        submissions = CVSubmission.objects.filter(id__in=ids)

        if action == "mark-processed":
            submissions.update(is_processed=True)
            message = f"{len(submissions)} submissions marked as processed"
        elif action == "mark-pending":
            submissions.update(is_processed=False)
            message = f"{len(submissions)} submissions marked as pending"
        elif action == "delete":
            count = submissions.count()
            submissions.delete()
            message = f"{count} submissions deleted"
        else:
            return JsonResponse({"success": False, "message": "Invalid action"})

        return JsonResponse({"success": True, "message": message})
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"})


@staff_member_required
def export_submissions(request):
    """Export CV submissions to CSV"""
    try:
        ids = request.GET.get("ids", "").split(",")
        if ids and ids[0]:
            submissions = CVSubmission.objects.filter(id__in=ids)
        else:
            submissions = CVSubmission.objects.all()

        # Create CSV response
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="cv_submissions.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "ID",
                "Name",
                "Email",
                "Phone",
                "Position",
                "Submitted Date",
                "Processed",
                "File Name",
                "File Size",
                "Cover Letter",
            ]
        )

        for submission in submissions:
            writer.writerow(
                [
                    submission.id,
                    submission.applicant_name,
                    submission.applicant_email,
                    submission.applicant_phone or "",
                    submission.position_applied or "",
                    submission.submitted_at.strftime("%Y-%m-%d %H:%M"),
                    "Yes" if submission.is_processed else "No",
                    submission.cv_file.name if submission.cv_file else "",
                    submission.get_file_size(),
                    submission.cover_letter or "",
                ]
            )

        return response
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Export error: {str(e)}"})


@staff_member_required
def cv_dashboard(request):
    """Custom dashboard for CV submissions"""
    try:
        # Get date range from request
        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        # Base queryset
        queryset = CVSubmission.objects.all()

        # Apply date filters
        if date_from:
            queryset = queryset.filter(submitted_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(submitted_at__lte=date_to)

        # Get statistics
        total = queryset.count()
        pending = queryset.filter(is_processed=False).count()
        processed = queryset.filter(is_processed=True).count()

        # Get recent submissions
        recent_submissions = queryset.order_by("-submitted_at")[:10]

        # Get submissions by position
        positions = (
            queryset.values("position_applied")
            .annotate(count=models.Count("id"))
            .order_by("-count")[:10]
        )

        context = {
            "total_submissions": total,
            "pending_submissions": pending,
            "processed_submissions": processed,
            "recent_submissions": recent_submissions,
            "positions": positions,
            "date_from": date_from,
            "date_to": date_to,
        }

        return render(request, "admin/pages/cvsubmission/dashboard.html", context)
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Dashboard error: {str(e)}"})


@staff_member_required
def cv_analytics(request):
    """Analytics view for CV submissions"""
    try:
        # Get date range
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=30)  # Last 30 days

        # Daily submissions
        daily_submissions = (
            CVSubmission.objects.filter(
                submitted_at__date__gte=start_date, submitted_at__date__lte=end_date
            )
            .extra(select={"day": "date(submitted_at)"})
            .values("day")
            .annotate(count=Count("id"))
            .order_by("day")
        )

        # Position statistics
        position_stats = (
            CVSubmission.objects.values("position_applied")
            .annotate(count=Count("id"))
            .order_by("-count")[:10]
        )

        # Processing status
        status_stats = CVSubmission.objects.values("is_processed").annotate(
            count=Count("id")
        )

        # Calculate total for percentage calculation
        total_submissions = CVSubmission.objects.count()

        context = {
            "daily_submissions": list(daily_submissions),
            "position_stats": list(position_stats),
            "status_stats": list(status_stats),
            "total_submissions": total_submissions,
            "start_date": start_date,
            "end_date": end_date,
        }

        return render(request, "admin/pages/cvsubmission/analytics.html", context)
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Analytics error: {str(e)}"})
