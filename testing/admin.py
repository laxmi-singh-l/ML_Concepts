from django.contrib import admin
from .models import TestTemplate, MetricEntry


@admin.register(TestTemplate)
class TestTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'test_type', 'difficulty', 'order']
    list_filter = ['test_type', 'difficulty']
    search_fields = ['name', 'description']
    ordering = ['test_type', 'order']


@admin.register(MetricEntry)
class MetricEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'metric_type', 'order']
    list_filter = ['metric_type']
    search_fields = ['name', 'description', 'formula']
    ordering = ['metric_type', 'order']