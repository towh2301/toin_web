# CV Submission Setup Guide

## Overview

The recruiter page has been updated with Toin's color scheme and includes a CV submission form that sends emails to `huy.buihoang.cit20@eiu.edu.vn`.

## Features Implemented

### 1. Template Updates

-   ✅ Rewritten recruiter template with Toin's green color scheme (`#006953`)
-   ✅ Responsive design with modern UI components
-   ✅ Interactive job cards with collapsible details
-   ✅ CV submission modal with form validation

### 2. CV Submission Model

-   ✅ `CVSubmission` model created with fields:
    -   `applicant_name` (required)
    -   `applicant_email` (required)
    -   `applicant_phone` (optional)
    -   `position_applied` (optional)
    -   `cover_letter` (optional)
    -   `cv_file` (required, PDF/DOC/DOCX, max 5MB)
    -   `submitted_at` (auto-generated)
    -   `is_processed` (for HR tracking)
    -   `notes` (internal notes)

### 3. Email Functionality

-   ✅ Sends notification email to HR (`huy.buihoang.cit20@eiu.edu.vn`)
-   ✅ Sends confirmation email to applicant
-   ✅ Attaches CV file to HR email
-   ✅ Uses Gmail SMTP (free service)

### 4. Admin Interface

-   ✅ CV submissions visible in Django admin
-   ✅ Filtering and search capabilities
-   ✅ Processing status tracking

## Email Configuration

To enable email sending, set these environment variables:

```bash
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@toin.com.vn
```

### Gmail Setup Instructions:

1. Enable 2-factor authentication on your Gmail account
2. Generate an "App Password" for Django
3. Use the app password (not your regular password) in `EMAIL_HOST_PASSWORD`

## Usage

1. **For Job Seekers:**

    - Visit the recruiter page
    - Click "Apply Now" on any job posting
    - Fill out the CV submission form
    - Upload CV file (PDF, DOC, or DOCX)
    - Submit the form

2. **For HR:**
    - Check Django admin for new submissions
    - Review applications and mark as processed
    - CV files are stored in `media/cv_submissions/`

## File Structure

```
media/
└── cv_submissions/          # Uploaded CV files
    ├── 2024/
    │   └── 01/
    │       └── filename.pdf
    └── ...

templates/pages/
└── recruiter.html           # Updated template with Toin colors
```

## Database Migration

The migration has been created and applied:

-   `pages/migrations/0023_cvsubmission.py`

## Testing

To test the CV submission:

1. Set up email credentials in environment variables
2. Run the development server: `python manage.py runserver`
3. Visit `/recruiter/` page
4. Try submitting a CV through the modal form
5. Check that emails are sent and database records are created
