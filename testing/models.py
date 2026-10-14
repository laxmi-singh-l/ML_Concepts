from django.db import models


class TestTemplate(models.Model):
    TEST_TYPE_CHOICES = [
        ('validation', 'Data Validation'),
        ('split', 'Train/Test Split'),
        ('cross_validation', 'Cross Validation'),
        ('overfitting', 'Overfitting Detection'),
        ('data_leakage', 'Data Leakage Check'),
        ('unit', 'Unit Testing'),
        ('metric', 'Metric Calculation'),
    ]

    test_type = models.CharField(max_length=30, choices=TEST_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    description = models.TextField()
    code_template = models.TextField()
    assertions = models.JSONField(default=list)
    libraries_needed = models.JSONField(default=list)
    difficulty = models.CharField(max_length=20, default='beginner')
    when_to_use = models.TextField()
    common_errors = models.JSONField(default=list)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['test_type', 'order']
        verbose_name = 'Test Template'
        verbose_name_plural = 'Test Templates'

    def __str__(self):
        return f"{self.get_test_type_display()}: {self.name}"


class MetricEntry(models.Model):
    METRIC_TYPE_CHOICES = [
        ('classification', 'Classification'),
        ('regression', 'Regression'),
        ('clustering', 'Clustering'),
        ('ranking', 'Ranking'),
    ]

    name = models.CharField(max_length=100)
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPE_CHOICES)
    formula = models.CharField(max_length=500)
    description = models.TextField()
    code_template = models.TextField()
    sklearn_function = models.CharField(max_length=200)
    range_info = models.CharField(max_length=200)
    when_to_use = models.TextField()
    common_pitfalls = models.JSONField(default=list)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['metric_type', 'order', 'name']
        verbose_name = 'Metric Entry'
        verbose_name_plural = 'Metric Entries'

    def __str__(self):
        return self.name