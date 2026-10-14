from django.urls import path
from . import views

app_name = 'pandas_numpy'

urlpatterns = [
    path('', views.function_list, name='function_list'),
    path('search/', views.search_functions, name='search'),
    path('playground/', views.playground, name='playground'),
    path('<str:library>/<str:name>/', views.function_detail, name='function_detail'),
]