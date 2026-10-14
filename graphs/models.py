from django.db import models


class ChartTemplate(models.Model):
    CHART_TYPES = [
        ('line', 'Line Chart'),
        ('bar', 'Bar Chart'),
        ('scatter', 'Scatter Plot'),
        ('histogram', 'Histogram'),
        ('box', 'Box Plot'),
        ('heatmap', 'Heatmap'),
        ('pie', 'Pie Chart'),
        ('area', 'Area Chart'),
    ]

    chart_type = models.CharField(max_length=20, choices=CHART_TYPES, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    use_case = models.TextField()
    input_schema = models.JSONField(default=dict, help_text="Defines expected input format")
    default_data = models.JSONField(default=dict)
    matplotlib_code = models.TextField()
    plotly_code = models.TextField()
    seaborn_code = models.TextField(blank=True)
    explanation = models.TextField()
    tips = models.JSONField(default=list)
    order = models.IntegerField(default=0)
    icon = models.CharField(max_length=50, default='graph-up')

    class Meta:
        ordering = ['order']
        verbose_name = 'Chart Template'
        verbose_name_plural = 'Chart Templates'

    def __str__(self):
        return self.name


class SavedChart(models.Model):
    chart_type = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    user_data = models.JSONField()
    chart_config = models.JSONField(default=dict)
    plotly_json = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.chart_type})"