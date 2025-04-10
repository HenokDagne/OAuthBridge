from django.urls import path, include
from djoser.views import TokenDestroyView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.routers import DefaultRouter

from .views import (
    Home,
    ProfileView,
    google_logout,
)


# Custom error handlers
handler404 = 'myapp.views.custom_404_view'
handler500 = 'myapp.views.custom_500_view'


# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'profile', ProfileView, basename='profile')



urlpatterns = [
    path('api/', include(router.urls)),
    path('', Home.as_view(), name='home'), 
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('auth/jwt/logout/', TokenDestroyView.as_view(), name='auth_jwt_logout'),
    path('accounts/google/logout/', google_logout, name='google_logout'),
]

