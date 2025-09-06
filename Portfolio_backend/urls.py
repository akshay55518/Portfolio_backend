from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Portfolio_App.urls')),
    path('', include('Portfolio_Admin_App.urls')),
    
]
if settings.DEBUG:  # only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)