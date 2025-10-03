from django.db import models


# Create your models here.
class Introduction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='intro/', blank=True, null=True)

    class Meta:
        verbose_name = "Introduction"
        verbose_name_plural = "Introduction"

    def __str__(self):
        return self.title
