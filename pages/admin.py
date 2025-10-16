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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["get_title", "is_published", "publish_date"]
    list_filter = ["is_published", "publish_date"]
    search_fields = ["en_title", "vi_title", "jp_title", "en_description"]
    readonly_fields = ["publish_date"]
    date_hierarchy = "publish_date"

    fieldsets = (
        (
            "Content",
            {
                "fields": (
                    "en_title",
                    "vi_title",
                    "jp_title",
                    "en_description",
                    "vi_description",
                    "jp_description",
                    "image",
                )
            },
        ),
        (
            "Publishing",
            {"fields": ("is_published", "publish_date")},
        ),
    )

    actions = ["publish_posts", "unpublish_posts"]

    def get_title(self, obj):
        return obj.get_title() or obj.en_title or "Unnamed"

    get_title.short_description = "Title"

    def publish_posts(self, request, queryset):
        from django.utils import timezone

        updated = queryset.update(is_published=True, publish_date=timezone.now())
        self.message_user(request, f"{updated} post(s) published.")

    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} post(s) unpublished.")

    unpublish_posts.short_description = "Unpublish selected posts"


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

    actions = ["mark_as_processed", "mark_as_pending", "export_as_csv"]

    def mark_as_processed(self, request, queryset):
        updated = queryset.update(is_processed=True)
        self.message_user(request, f"{updated} submission(s) marked as processed.")

    mark_as_processed.short_description = "Mark selected submissions as processed"

    def mark_as_pending(self, request, queryset):
        updated = queryset.update(is_processed=False)
        self.message_user(request, f"{updated} submission(s) marked as pending.")

    mark_as_pending.short_description = "Mark selected submissions as pending"

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="cv_submissions_export.csv"'
        )

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
            ]
        )

        for s in queryset:
            writer.writerow(
                [
                    s.id,
                    s.applicant_name,
                    s.applicant_email,
                    s.applicant_phone or "",
                    s.position_applied or "",
                    s.submitted_at.strftime("%Y-%m-%d %H:%M"),
                    "Yes" if s.is_processed else "No",
                ]
            )

        return response

    export_as_csv.short_description = "Export selected submissions as CSV"

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
