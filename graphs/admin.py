from django.contrib import admin
from .models import ChartTemplate, SavedChart


@admin.register(ChartTemplate)
class ChartTemplateAdmin(admin.ModelAdmin):
    list_display = ['chart_type', 'name', 'order']
    list_filter = ['chart_type']
    search_fields = ['name', 'description']
    fieldsets = (
        (None, {'fields': ('chart_type', 'name', 'description', 'use_case', 'order', 'icon')}),
        ('Data Schema', {'fields': ('input_schema', 'default_data')}),
        ('Code Templates', {'fields': ('matplotlib_code', 'plotly_code', 'seaborn_code')}),
        ('Help', {'fields': ('explanation', 'tips')}),
    )


@admin.register(SavedChart)
class SavedChartAdmin(admin.ModelAdmin):
    list_display = ['title', 'chart_type', 'created_at']
    list_filter = ['chart_type']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']