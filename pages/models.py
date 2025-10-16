from django.db import models
from django.utils.translation import get_language


# Hero model for introductory content
class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="intro/", blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Hero"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


# Post model for blog or news content
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="post/", blank=True, null=True)
    is_published = models.BooleanField(
        default=False, help_text="Publish this post to make it visible on the blog"
    )
    publish_date = models.DateTimeField(
        null=True, blank=True, help_text="Date and time when this post was published"
    )

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Post"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )

    def get_title(self):
        language = get_language()
        return getattr(self, f"{language}_title", None)


# Business model for business-related content
class Business(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="business/", blank=True, null=True)
    map = models.FileField(upload_to="map/", blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Business"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


# Feature model for showcasing features with PDFs
class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to="feature/", blank=True, null=True)
    image = models.FileField(upload_to="feature/", blank=True, null=True)
    web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Feature"

    def get_title(self):
        language = get_language()
        return getattr(self, f"{language}_title", None)

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(
        max_length=1,
        choices=[
            ("P", "Packages"),
            ("L", "Labels"),
            ("I", "Instructions"),
            ("T", "Technologies"),
        ],
        default="P",
    )

    def get_title(self):
        language = get_language()
        return getattr(self, f"{language}_title", None)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Type"


# Product model for product listings
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(
        "Type", on_delete=models.CASCADE, related_name="products", default=1
    )
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="product/", blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Product"

    def get_title(self):
        language = get_language()
        return getattr(self, f"{language}_title", None)

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


# ParentCorporation model to store multiple parent entities
class ParentCorporation(models.Model):
    id = models.AutoField(primary_key=True)
    company_profile = models.ForeignKey(
        "CompanyProfile", on_delete=models.CASCADE, related_name="parent_corporations"
    )
    en_name = models.CharField(null=True, blank=True, max_length=200)
    vi_name = models.CharField(null=True, blank=True, max_length=200)
    jp_name = models.CharField(null=True, blank=True, max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return (
            self.en_name or self.vi_name or self.jp_name or "Unnamed Parent Corporation"
        )

    def get_name(self):
        from django.utils.translation import get_language

        language = get_language()
        return (
            getattr(self, f"{language}_name", None)
            or self.en_name
            or self.vi_name
            or self.jp_name
            or "Unnamed Parent Corporation"
        )


# CompanyProfile model for company details
class CompanyProfile(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    foundation_date = models.DateField()
    representative = models.CharField(max_length=100)
    capital = models.DecimalField(max_digits=12, decimal_places=2)
    en_mission = models.CharField(max_length=200, null=True, blank=True)
    vi_mission = models.CharField(max_length=200, null=True, blank=True)
    jp_mission = models.CharField(max_length=200, null=True, blank=True)
    en_productions_operations = models.TextField(null=True, blank=True)
    vi_productions_operations = models.TextField(null=True, blank=True)
    jp_productions_operations = models.TextField(null=True, blank=True)
    en_address = models.TextField(null=False, blank=False, default="No Data")
    vi_address = models.TextField(null=False, blank=False, default="No Data")
    jp_address = models.TextField(null=False, blank=False, default="No Data")

    def get_productions_operations(self):
        language = get_language()
        return getattr(self, f"{language}_productions_operations", None) or "No Data"

    def get_address(self):
        language = get_language()
        return getattr(self, f"{language}_address", None) or "No Data"

    def get_mission(self):
        language = get_language()
        return getattr(self, f"{language}_mission", None) or "No Data"

    def __str__(self):
        return self.company_name


# History model for company history
class History(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"History - {self.year}" if self.year else "Unnamed History"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


# Progress model for progress updates
class Progress(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Progress"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    company_profile = models.ForeignKey(
        "CompanyProfile", on_delete=models.CASCADE, related_name="office_addresses"
    )
    en_name = models.CharField(max_length=200, null=True, blank=True)
    vi_name = models.CharField(max_length=200, null=True, blank=True)
    jp_name = models.CharField(max_length=200, null=True, blank=True)
    en_address = models.TextField(null=False, blank=False, default="No Data")
    vi_address = models.TextField(null=False, blank=False, default="No Data")
    jp_address = models.TextField(null=False, blank=False, default="No Data")
    address_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.en_name or self.vi_name or self.jp_name or "No Address Link"

    def get_name(self):
        language = get_language()
        return getattr(self, f"{language}_name", None) or "No Address"

    def get_address(self):
        language = get_language()
        return getattr(self, f"{language}_address", None) or "No Data"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey(
        "Address", on_delete=models.CASCADE, related_name="contact_addresses"
    )
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    contact_name = models.CharField(
        max_length=200, null=False, blank=False, default="No Data"
    )
    contact_number = models.CharField(
        max_length=200, null=False, blank=False, default="No Data"
    )
    contact_email = models.CharField(
        max_length=200, null=False, blank=False, default="No Data"
    )

    def __str__(self):
        return self.contact_name

    def get_full_details(self):
        if self.gender == "M":
            return f"{self.contact_name}(Mr): {self.contact_number}"
        elif self.gender == "F":
            return f"{self.contact_name}(Mrs): {self.contact_number}"
        return None

    def get_contact(self):
        return f"{self.contact_name}: {self.contact_number}"


class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(max_length=200, null=True, blank=True)
    vi_name = models.CharField(max_length=200, null=True, blank=True)
    jp_name = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    en_address = models.TextField(null=True, blank=True)
    vi_address = models.TextField(null=True, blank=True)
    jp_address = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="partner/", blank=True, null=True)

    def __str__(self):
        return self.en_name or self.vi_name or self.jp_name or "Unnamed Partner"

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )

    def get_address(self):
        language = get_language()
        return (
            getattr(self, f"{language}_address", None)
            or getattr(self, "en_address", None)
            or getattr(self, "vi_address", None)
            or getattr(self, "jp_address", None)
            or "No address available"
        )

    def get_name(self):
        language = get_language()
        return (
            getattr(self, f"{language}_name", None)
            or self.en_name
            or self.vi_name
            or self.jp_name
            or "Unnamed Partner"
        )


# Recruiter model for job postings and recruitment content
class Recruiter(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    en_requirements = models.TextField(null=True, blank=True)
    vi_requirements = models.TextField(null=True, blank=True)
    jp_requirements = models.TextField(null=True, blank=True)
    en_benefits = models.TextField(null=True, blank=True)
    vi_benefits = models.TextField(null=True, blank=True)
    jp_benefits = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    employment_type = models.CharField(
        max_length=20,
        choices=[
            ("FULL_TIME", "Full Time"),
            ("PART_TIME", "Part Time"),
            ("CONTRACT", "Contract"),
            ("INTERNSHIP", "Internship"),
        ],
        default="FULL_TIME",
    )
    experience_level = models.CharField(
        max_length=20,
        choices=[
            ("ENTRY", "Entry Level"),
            ("JUNIOR", "Junior"),
            ("MID", "Mid Level"),
            ("SENIOR", "Senior"),
            ("LEAD", "Lead"),
        ],
        default="ENTRY",
    )
    department = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.FileField(upload_to="recruiter/", blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Position"

    def get_title(self):
        language = get_language()
        return (
            getattr(self, f"{language}_title", None)
            or getattr(self, "en_title", None)
            or getattr(self, "vi_title", None)
            or getattr(self, "jp_title", None)
            or "No title available"
        )

    def get_description(self):
        language = get_language()
        return (
            getattr(self, f"{language}_description", None)
            or getattr(self, "en_description", None)
            or getattr(self, "vi_description", None)
            or getattr(self, "jp_description", None)
            or "No description available"
        )

    def get_requirements(self):
        language = get_language()
        return (
            getattr(self, f"{language}_requirements", None)
            or getattr(self, "en_requirements", None)
            or getattr(self, "vi_requirements", None)
            or getattr(self, "jp_requirements", None)
            or "No requirements available"
        )

    def get_benefits(self):
        language = get_language()
        return (
            getattr(self, f"{language}_benefits", None)
            or getattr(self, "en_benefits", None)
            or getattr(self, "vi_benefits", None)
            or getattr(self, "jp_benefits", None)
            or "No benefits available"
        )


# CV Submission model for handling job applications
class CVSubmission(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_name = models.CharField(max_length=200, verbose_name="Full Name")
    applicant_email = models.EmailField(verbose_name="Email Address")
    applicant_phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Phone Number"
    )
    position_applied = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Position Applied For"
    )
    cover_letter = models.TextField(blank=True, null=True, verbose_name="Cover Letter")
    cv_file = models.FileField(
        upload_to="cv_submissions/", verbose_name="CV/Resume File"
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Submission Date"
    )
    is_processed = models.BooleanField(default=False, verbose_name="Processed")
    notes = models.TextField(blank=True, null=True, verbose_name="Internal Notes")

    class Meta:
        verbose_name = "CV Submission"
        verbose_name_plural = "CV Submissions"
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.applicant_name} - {self.position_applied or 'General Application'} ({self.submitted_at.strftime('%Y-%m-%d')})"

    def get_file_size(self):
        """Return file size in human readable format"""
        if self.cv_file:
            size = self.cv_file.size
            for unit in ["B", "KB", "MB", "GB"]:
                if size < 1024.0:
                    return f"{size:.1f} {unit}"
                size /= 1024.0
        return "Unknown"
