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
    image = models.FileField(upload_to='intro/', blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Hero"

    def get_description(self):
        language = get_language()
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


# Post model for blog or news content
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='post/', blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Post"

    def get_description(self):
        language = get_language()
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


# Business model for business-related content
class Business(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='business/', blank=True, null=True)
    map = models.FileField(upload_to='map/', blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Business"

    def get_description(self):
        language = get_language()
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


# Feature model for showcasing features with PDFs
class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='feature/', blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Feature"

    def get_description(self):
        language = get_language()
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


# Product model for product listings
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='product/', blank=True, null=True)

    def __str__(self):
        return self.en_title or self.vi_title or self.jp_title or "Unnamed Product"

    def get_description(self):
        language = get_language()
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


# ParentCorporation model to store multiple parent entities
class ParentCorporation(models.Model):
    company_profile = models.ForeignKey('CompanyProfile', on_delete=models.CASCADE, related_name='parent_corporations')
    en_name = models.CharField(null=True, blank=True, max_length=200)
    vi_name = models.CharField(null=True, blank=True, max_length=200)
    jp_name = models.CharField(null=True, blank=True, max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.en_name or self.vi_name or self.jp_name or "Unnamed Parent Corporation"

    def get_name(self):
        from django.utils.translation import get_language
        language = get_language()
        return getattr(self, f'{language}_name',
                       None) or self.en_name or self.vi_name or self.jp_name or "Unnamed Parent Corporation"


# CompanyProfile model for company details
class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=200)
    foundation_date = models.DateField()
    representative = models.CharField(max_length=100)
    capital = models.DecimalField(max_digits=12, decimal_places=2)
    en_productions_operations = models.TextField(null=True, blank=True)
    vi_productions_operations = models.TextField(null=True, blank=True)
    jp_productions_operations = models.TextField(null=True, blank=True)
    en_address = models.TextField(null=False, blank=False, default='No Data')
    vi_address = models.TextField(null=False, blank=False, default='No Data')
    jp_address = models.TextField(null=False, blank=False, default='No Data')

    def get_productions_operations(self):
        language = get_language()
        return getattr(self, f'{language}_productions_operations', None) or "No Data"

    def get_address(self):
        language = get_language()
        return getattr(self, f'{language}_productions_operations', None) or "No Data"

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
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"


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
        return getattr(self, f'{language}_description', None) or \
            getattr(self, 'en_description', None) or \
            getattr(self, 'vi_description', None) or \
            getattr(self, 'jp_description', None) or \
            "No description available"
