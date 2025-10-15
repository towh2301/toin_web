# Recruiter Page - TOIN Vietnam

## Overview

The recruiter page has been successfully created for the TOIN Vietnam website. This page allows the company to post job openings and manage recruitment content.

## Features

### 1. Recruiter Model

-   **Multi-language support**: English, Vietnamese, and Japanese
-   **Job details**: Title, description, requirements, benefits
-   **Job metadata**: Salary range, location, employment type, experience level, department
-   **Status management**: Active/inactive job postings
-   **Timestamps**: Created and updated dates
-   **Image support**: Optional job posting images

### 2. Admin Interface

-   Full admin interface for managing job postings
-   Easy content management for HR team
-   Multi-language field support

### 3. Frontend Features

-   **Responsive design**: Works on all devices
-   **Job cards**: Clean, professional job posting cards
-   **Expandable details**: Click to view full job descriptions
-   **Filtering**: By employment type and experience level
-   **Contact section**: Easy application process
-   **Empty state**: Professional message when no jobs are available

## URL Structure

-   **Main recruiter page**: `/recruiter/`
-   **Admin interface**: `/admin/` (login required)

## Usage

### Adding Job Postings

1. Go to Django Admin (`/admin/`)
2. Navigate to "Recruiters" section
3. Click "Add Recruiter"
4. Fill in job details in your preferred language(s)
5. Set job as active
6. Save the posting

### Job Posting Fields

-   **Title**: Job title in multiple languages
-   **Description**: Detailed job description
-   **Requirements**: Required skills and qualifications
-   **Benefits**: Company benefits and perks
-   **Salary Range**: Optional salary information
-   **Location**: Job location
-   **Employment Type**: Full-time, Part-time, Contract, Internship
-   **Experience Level**: Entry, Junior, Mid, Senior, Lead
-   **Department**: Company department
-   **Image**: Optional job-related image

## Technical Implementation

### Models

-   `Recruiter`: Main model for job postings
-   Multi-language support with `get_title()`, `get_description()`, `get_requirements()`, `get_benefits()` methods

### Views

-   `recruiter()`: Displays all active job postings
-   Filters by `is_active=True`
-   Orders by creation date (newest first)

### Templates

-   `templates/pages/recruiter.html`: Main recruiter page template
-   Responsive Bootstrap-based design
-   AOS animations for smooth user experience

### URLs

-   Added to `pages/urls.py`: `path("recruiter/", views.recruiter, name="recruiter")`

## Database Migration

-   Migration file: `pages/migrations/0020_recruiter.py`
-   Successfully applied to database

## Styling

-   Uses existing Bootstrap framework
-   Consistent with site design
-   Professional job posting cards
-   Mobile-responsive layout

## Future Enhancements

-   Job application form integration
-   Email notifications for new applications
-   Job categories and tags
-   Search functionality
-   Advanced filtering options
-   Application tracking system

## Access

-   **Public URL**: `http://localhost:8000/vi/recruiter/`
-   **Admin URL**: `http://localhost:8000/vi/admin/`

The recruiter page is now fully functional and ready for use!
