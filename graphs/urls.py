from django.urls import path
from . import views

app_name = 'graphs'

urlpatterns = [
    path('', views.chart_list, name='chart_list'),
    path('builder/', views.chart_builder, name='chart_builder'),
    path('builder/<str:chart_type>/', views.chart_builder, name='chart_builder_type'),
    path('api/generate-code/', views.generate_code, name='generate_code'),
    path('api/save-chart/', views.save_chart, name='save_chart'),
    path('download/', views.download_code, name='download_code'),
    path('saved/', views.saved_charts, name='saved_charts'),
]