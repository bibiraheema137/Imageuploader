from django.contrib import admin
from .models import UploadedImage  # Import your model

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')  # Display only necessary fields
    actions = ['delete_selected']  # Enable bulk delete

    def delete_selected(self, request, queryset):
        queryset.delete()
    delete_selected.short_description = "Delete selected images"
