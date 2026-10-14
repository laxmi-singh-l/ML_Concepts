from django.db import models


class MLModel(models.Model):
    CATEGORY_CHOICES = [
        ('linear', 'Linear Models'),
        ('tree', 'Tree-Based'),
        ('ensemble', 'Ensemble Methods'),
        ('boosting', 'Gradient Boosting'),
        ('svm', 'Support Vector Machines'),
        ('neighbors', 'Instance-Based'),
        ('naive_bayes', 'Probabilistic'),
        ('neural_network', 'Neural Networks'),
        ('clustering', 'Clustering'),
        ('dimensionality', 'Dimensionality Reduction'),
        ('anomaly', 'Anomaly Detection'),
    ]

    PROBLEM_TYPE_CHOICES = [
        ('classification', 'Classification'),
        ('regression', 'Regression'),
        ('clustering', 'Clustering'),
        ('dimensionality_reduction', 'Dimensionality Reduction'),
        ('anomaly_detection', 'Anomaly Detection'),
        ('generation', 'Generation'),
    ]

    COMPLEXITY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    SPEED_CHOICES = [
        ('fast', 'Fast'),
        ('medium', 'Medium'),
        ('slow', 'Slow'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    problem_types = models.JSONField(default=list)
    description = models.TextField()
    functionality = models.TextField()
    when_to_use = models.TextField()
    pros = models.JSONField(default=list)
    cons = models.JSONField(default=list)
    starter_code = models.TextField()
    full_training_code = models.TextField()
    hyperparameter_guide = models.JSONField(default=list)
    complexity = models.CharField(max_length=20, choices=COMPLEXITY_CHOICES, default='beginner')
    speed_rating = models.CharField(max_length=10, choices=SPEED_CHOICES, default='fast')
    accuracy_notes = models.TextField(blank=True)
    sklearn_import = models.CharField(max_length=200)
    related_libraries = models.JSONField(default=list)
    math_intuition = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'ML Model'
        verbose_name_plural = 'ML Models'

    def __str__(self):
        return self.name

    def get_problem_type_badge_color(self):
        colors = {
            'classification': 'primary',
            'regression': 'success',
            'clustering': 'warning',
            'dimensionality_reduction': 'info',
            'anomaly_detection': 'danger',
            'generation': 'secondary',
        }
        return colors


class Hyperparameter(models.Model):
    TYPE_CHOICES = [
        ('int', 'Integer'),
        ('float', 'Float'),
        ('str', 'String/Choice'),
        ('bool', 'Boolean'),
    ]

    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name='hyperparams')
    name = models.CharField(max_length=100)
    param_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    default = models.CharField(max_length=100)
    description = models.TextField()
    recommended_range = models.CharField(max_length=200, blank=True)
    impact = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['model', 'order']
        verbose_name = 'Hyperparameter'
        verbose_name_plural = 'Hyperparameters'

    def __str__(self):
        return f"{self.model.name}.{self.name}"