from django.urls import path, include
from socialNetwork import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'post', views.PostViewSet)
router.register(r'analytics', views.LikeViewSet)
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
