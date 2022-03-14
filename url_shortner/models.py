from django.db import models

# Create your models here.

class Urls(models.Model):
    original_url = models.CharField(max_length=512)
    shortened_url = models.CharField(max_length=64, unique=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Urls"
