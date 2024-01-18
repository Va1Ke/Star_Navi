from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from socialNetwork.api.mixins import LikeModelMixin
from socialNetwork.api.serializers import PostSerializer, LikeSerializer, UserSerializer, CustomObtainPairSerializer
from socialNetwork.filters import LikeFilterSet
from socialNetwork.forms import UserRegistrationForm
from socialNetwork.models import Post, Like, User
from rest_framework_simplejwt.views import TokenObtainPairView


def user_register(request):
    if request.method == 'POST':
        User.objects.create_user(username=str(request.POST['username']),
                                 email=str(request.POST['email']),
                                 password=str(request.POST['password1']))
        return redirect('/star-navi/api/token/')

    form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomObtainPairSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


@extend_schema_view(
    list=extend_schema(
        description='List posts'
    ),
    create=extend_schema(
        description='Create post'
    ),
    retrieve=extend_schema(
        description='Retrieve post'
    ),
    update=extend_schema(
        description='Put post'
    ),
    partial_update=extend_schema(
        description='Patch post'
    ),
    destroy=extend_schema(
        description='Delete post'
    )
)
class PostViewSet(LikeModelMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()


class LikeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeFilterSet
