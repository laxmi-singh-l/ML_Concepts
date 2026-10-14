from django.contrib import admin
from .models import MLModel, Hyperparameter


class HyperparameterInline(admin.TabularInline):
    model = Hyperparameter
    extra = 1
    fields = ['name', 'param_type', 'default', 'order']
    ordering = ['order']


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'complexity', 'speed_rating', 'is_featured', 'created_at']
    list_filter = ['category', 'complexity', 'speed_rating', 'is_featured']
    search_fields = ['name', 'description', 'functionality']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HyperparameterInline]
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'category', 'problem_types', 'complexity', 'speed_rating', 'is_featured', 'order')}),
        ('Descriptions', {'fields': ('description', 'functionality', 'when_to_use', 'accuracy_notes', 'math_intuition')}),
        ('Pros & Cons', {'fields': ('pros', 'cons')}),
        ('Code', {'fields': ('starter_code', 'full_training_code', 'sklearn_import', 'related_libraries')}),
    )


@admin.register(Hyperparameter)
class HyperparameterAdmin(admin.ModelAdmin):
    list_display = ['model', 'name', 'param_type', 'default', 'order']
    list_filter = ['param_type', 'model__category']
    search_fields = ['name', 'model__name']
    ordering = ['model', 'order']