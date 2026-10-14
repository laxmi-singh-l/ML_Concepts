"""Main URL configuration for ml_concepts project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('libraries/', include('ml_libraries.urls')),
    path('graphs/', include('graphs.urls')),
    path('pandas-numpy/', include('pandas_numpy.urls')),
    path('models/', include('ml_models.urls')),
    path('testing/', include('testing.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)