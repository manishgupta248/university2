from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course
from .resources import CourseResource

# Register your models here.

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ('code','name', 'category', 'type', 'cbcs_category', 'maximum_credit')
    ordering = ('code',)
    search_fields = ('name', 'code', 'type')
    list_filter = ('type', 'category', 'cbcs_category',)