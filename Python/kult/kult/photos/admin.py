from django.contrib import admin

from .models import Photo, PhotoDescription


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('upload', 'upload_date')
    search_fields = ['upload_date']
    ordering = ['upload_date']


class PhotoDescriptionAdmin(admin.ModelAdmin):
    list_display = ('photo', 'desc_type', 'description')
    search_fields = ['desc_type', 'description']
    ordering = ['desc_type']

# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoDescription, PhotoDescriptionAdmin)
