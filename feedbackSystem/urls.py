from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('client/', include('client_app.urls')),  # Client app routes
    path('admin-app/', include('admin_app.urls')),  # Admin app routes
    path('accounts/', include('allauth.urls')),  # Allauth routes for authentication
]
