from django.contrib import admin
from .models import UserProgress, UserNote


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_module', 'completed_count', 'updated_at']
    list_filter = ['current_module']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']

    def completed_count(self, obj):
        return len(obj.completed_modules)
    completed_count.short_description = 'Completed Modules'


@admin.register(UserNote)
class UserNoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'module_slug', 'section', 'created_at']
    list_filter = ['module_slug']
    search_fields = ['user__username', 'content']
    readonly_fields = ['created_at', 'updated_at']