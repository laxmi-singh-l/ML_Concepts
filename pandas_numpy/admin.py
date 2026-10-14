from django.contrib import admin
from .models import FunctionEntry


@admin.register(FunctionEntry)
class FunctionEntryAdmin(admin.ModelAdmin):
    list_display = ['library', 'name', 'category', 'difficulty', 'is_popular']
    list_filter = ['library', 'category', 'difficulty', 'is_popular']
    search_fields = ['name', 'signature', 'short_description']
    prepopulated_fields = {'name': ('short_description',)}
    fieldsets = (
        (None, {'fields': ('library', 'category', 'name', 'signature', 'difficulty', 'is_popular', 'order')}),
        ('Descriptions', {'fields': ('short_description', 'long_description')}),
        ('Code', {'fields': ('example_code', 'expected_output', 'test_code')}),
        ('Extras', {'fields': ('common_mistakes', 'related_functions')}),
    )