from django.db import models


# Create your models here.
class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='intro/', blank=True, null=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='post/', blank=True, null=True)


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


class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(max_length=200, null=True, blank=True)
    vi_title = models.CharField(max_length=200, null=True, blank=True)
    jp_title = models.CharField(max_length=200, null=True, blank=True)
    en_description = models.TextField(null=True, blank=True)
    vi_description = models.TextField(null=True, blank=True)
    jp_description = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='feature/', blank=True, null=True)
