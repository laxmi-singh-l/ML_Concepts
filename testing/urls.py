from django.urls import path
from . import views

app_name = 'testing'

urlpatterns = [
    path('', views.test_generator, name='test_generator'),
    path('metrics/', views.metric_library, name='metric_library'),
    path('validation/', views.validation_patterns, name='validation_patterns'),
]