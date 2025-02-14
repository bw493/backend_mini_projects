from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comments.urls')),  # this line points the root URL to your comments app
]