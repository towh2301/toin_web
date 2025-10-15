from django.contrib import admin
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
    ParentCorporation,
    Address,
    Contact,
    Type,
    Recruiter,
    CVSubmission,
)

admin.site.register(Hero)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(CompanyProfile)
admin.site.register(History)
admin.site.register(Progress)
admin.site.register(ParentCorporation)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Type)
admin.site.register(Partner)
admin.site.register(Recruiter)


@admin.register(CVSubmission)
class CVSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "applicant_name",
        "applicant_email",
        "position_applied",
        "submitted_at",
        "is_processed",
    ]
    list_filter = ["is_processed", "submitted_at", "position_applied"]
    search_fields = ["applicant_name", "applicant_email", "position_applied"]
    readonly_fields = ["submitted_at"]
    list_editable = ["is_processed"]
    date_hierarchy = "submitted_at"
    change_list_template = "admin/pages/cvsubmission/change_list.html"
    change_form_template = "admin/pages/cvsubmission/change_form.html"

    fieldsets = (
        (
            "Applicant Information",
            {
                "fields": (
                    "applicant_name",
                    "applicant_email",
                    "applicant_phone",
                    "position_applied",
                )
            },
        ),
        (
            "Application Details",
            {"fields": ("cover_letter", "cv_file", "submitted_at")},
        ),
        ("Processing", {"fields": ("is_processed", "notes"), "classes": ("collapse",)}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        # Get statistics for dashboard
        from django.utils import timezone
        from datetime import timedelta

        today = timezone.now().date()
        this_week_start = today - timedelta(days=today.weekday())

        queryset = self.get_queryset(request)

        extra_context.update(
            {
                "total_submissions": queryset.count(),
                "pending_submissions": queryset.filter(is_processed=False).count(),
                "processed_submissions": queryset.filter(is_processed=True).count(),
                "this_week_submissions": queryset.filter(
                    submitted_at__gte=this_week_start
                ).count(),
                "today": today,
                "this_week_start": this_week_start,
            }
        )

        return super().changelist_view(request, extra_context)
