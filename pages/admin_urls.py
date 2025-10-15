from django.urls import path
from . import admin_views

app_name = "cv_admin"

urlpatterns = [
    # Individual submission actions
    path(
        "<int:submission_id>/mark-processed/",
        admin_views.mark_processed,
        name="mark_processed",
    ),
    path(
        "<int:submission_id>/mark-pending/",
        admin_views.mark_pending,
        name="mark_pending",
    ),
    path(
        "<int:submission_id>/update-notes/",
        admin_views.update_notes,
        name="update_notes",
    ),
    # Bulk actions
    path("bulk-action/", admin_views.bulk_action, name="bulk_action"),
    # Export and analytics
    path("export/", admin_views.export_submissions, name="export_submissions"),
    path("dashboard/", admin_views.cv_dashboard, name="dashboard"),
    path("analytics/", admin_views.cv_analytics, name="analytics"),
]
