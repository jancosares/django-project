from django.urls import path
from .views import admin_dashboard, admin_login, admin_signup

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('login/', admin_login, name='admin_login'),
    path('signup/', admin_signup, name='admin_signup'),
]
