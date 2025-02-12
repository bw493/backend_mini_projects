from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include('api.urls')),  # Include API URLs
    path('', include('myapp.urls')),  # Include myapp URLs at the root
]