from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegisterView

urlpatterns = [
    path('authentication/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
    path('register/', RegisterView.as_view(), name='register'),
]
