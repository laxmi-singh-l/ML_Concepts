from django.urls import path
from . import views

app_name = 'ml_models'

urlpatterns = [
    path('', views.model_catalog, name='model_catalog'),
    path('compare/', views.model_compare, name='model_compare'),
    path('<slug:slug>/', views.model_detail, name='model_detail'),
]