from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Portfolio_App.urls')),
    path('', include('Portfolio_Admin_App.urls')),
    
]
