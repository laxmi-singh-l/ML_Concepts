from django.db import models


class FunctionEntry(models.Model):
    LIBRARY_CHOICES = [
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
    ]

    CATEGORY_CHOICES = [
        ('dataframe', 'DataFrame Operations'),
        ('series', 'Series Operations'),
        ('io', 'Input/Output'),
        ('grouping', 'Grouping & Aggregation'),
        ('merging', 'Merging & Joining'),
        ('reshaping', 'Reshaping & Pivoting'),
        ('string', 'String Methods'),
        ('datetime', 'DateTime Operations'),
        ('missing', 'Missing Data'),
        ('array_creation', 'Array Creation'),
        ('math', 'Math Operations'),
        ('stats', 'Statistics'),
        ('linear_algebra', 'Linear Algebra'),
        ('random', 'Random Numbers'),
        ('manipulation', 'Array Manipulation'),
        ('broadcasting', 'Broadcasting'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    library = models.CharField(max_length=10, choices=LIBRARY_CHOICES)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    signature = models.CharField(max_length=500)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(blank=True)
    example_code = models.TextField()
    expected_output = models.TextField(blank=True)
    test_code = models.TextField(blank=True)
    common_mistakes = models.JSONField(default=list)
    related_functions = models.JSONField(default=list)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    order = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['library', 'category', 'order', 'name']
        unique_together = ['library', 'name']
        verbose_name = 'Function Entry'
        verbose_name_plural = 'Function Entries'

    def __str__(self):
        return f"{self.library}.{self.name}"