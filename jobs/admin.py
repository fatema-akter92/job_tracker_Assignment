from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'position', 'status',
        'application_date', 'deadline',
    )
    list_filter = ('status',)
    search_fields = ('company_name', 'position')
