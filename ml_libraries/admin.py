from django.contrib import admin
from .models import MLibrary, TrainingStep, LibraryComparison


class TrainingStepInline(admin.TabularInline):
    model = TrainingStep
    extra = 1
    fields = ['step_type', 'title', 'order', 'is_optional']
    ordering = ['order']


@admin.register(MLibrary)
class MLibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TrainingStepInline]
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'category', 'description', 'long_description')}),
        ('Installation & Usage', {'fields': ('install_command', 'import_statement', 'version_check_code', 'hello_world_code')}),
        ('Features', {'fields': ('key_features', 'use_cases', 'pros', 'cons')}),
        ('Links', {'fields': ('documentation_url', 'github_url')}),
        ('Settings', {'fields': ('order', 'is_active')}),
    )


@admin.register(TrainingStep)
class TrainingStepAdmin(admin.ModelAdmin):
    list_display = ['library', 'step_type', 'title', 'order', 'is_optional']
    list_filter = ['step_type', 'is_optional', 'library__category']
    search_fields = ['title', 'description', 'library__name']
    ordering = ['library', 'order']


@admin.register(LibraryComparison)
class LibraryComparisonAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    filter_horizontal = ['libraries']