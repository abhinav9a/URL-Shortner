from django.contrib import admin

from url_shortner.models import Urls

# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ['shortened_url', 'original_url', 'created_date', 'updated_date']
    list_filter = ['shortened_url', 'original_url']
    search_fields = ['shortened_url', 'original_url']

admin.site.register(Urls, UrlAdmin)