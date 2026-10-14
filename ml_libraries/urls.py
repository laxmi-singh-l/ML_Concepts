from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('comparison/', views.library_comparison, name='comparison'),
    path('pipeline/', views.training_pipeline, name='training_pipeline'),
    path('<slug:slug>/', views.library_detail, name='library_detail'),
    path('<slug:slug>/note/', views.save_library_note, name='save_note'),
]