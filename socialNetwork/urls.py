from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from . import views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('api/', include('socialNetwork.api.urls')),
    path('register', views.user_register, name='register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
