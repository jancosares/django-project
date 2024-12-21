from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet, client_login, client_signup

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API routes
    path('login/', client_login, name='client_login'),  # Login page
    path('signup/', client_signup, name='client_signup'),  # Signup page
]
