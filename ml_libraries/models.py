from django.db import models


class MLibrary(models.Model):
    CATEGORY_CHOICES = [
        ('classical', 'Classical ML'),
        ('deep_learning', 'Deep Learning'),
        ('gradient_boosting', 'Gradient Boosting'),
        ('data_manipulation', 'Data Manipulation'),
        ('visualization', 'Visualization'),
        ('deployment', 'Deployment'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    install_command = models.CharField(max_length=200)
    import_statement = models.CharField(max_length=200)
    version_check_code = models.TextField(blank=True)
    hello_world_code = models.TextField()
    key_features = models.JSONField(default=list)
    use_cases = models.JSONField(default=list)
    pros = models.JSONField(default=list)
    cons = models.JSONField(default=list)
    documentation_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'ML Library'
        verbose_name_plural = 'ML Libraries'

    def __str__(self):
        return self.name


class TrainingStep(models.Model):
    STEP_TYPES = [
        ('setup', 'Setup & Imports'),
        ('data_loading', 'Data Loading'),
        ('preprocessing', 'Preprocessing'),
        ('feature_engineering', 'Feature Engineering'),
        ('model_selection', 'Model Selection'),
        ('training', 'Training'),
        ('evaluation', 'Evaluation'),
        ('tuning', 'Hyperparameter Tuning'),
        ('deployment', 'Deployment'),
    ]

    library = models.ForeignKey(MLibrary, on_delete=models.CASCADE, related_name='training_steps')
    step_type = models.CharField(max_length=30, choices=STEP_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_template = models.TextField()
    explanation = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_optional = models.BooleanField(default=False)
    tips = models.JSONField(default=list)
    common_pitfalls = models.JSONField(default=list)

    class Meta:
        ordering = ['library', 'order']
        verbose_name = 'Training Step'
        verbose_name_plural = 'Training Steps'

    def __str__(self):
        return f"{self.library.name} - {self.title}"


class LibraryComparison(models.Model):
    name = models.CharField(max_length=200)
    libraries = models.ManyToManyField(MLibrary, related_name='comparisons')
    criteria = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name