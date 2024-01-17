from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.utils import timezone
from socialNetwork.models import User, Post, Like
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta


@pytest.mark.django_db
class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@gmail.com', password='test1234')
        self.api = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.api.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.post = Post.objects.create(title='test1', body='test1_body', author=self.user)
        self.current_date = timezone.now()
        self.one_day_ago = (self.current_date - timedelta(days=1)).strftime('%Y-%m-%d')
        self.one_day_after = (self.current_date + timedelta(days=1)).strftime('%Y-%m-%d')
        self.current_date = self.current_date.strftime('%Y-%m-%d')

    def test_authorization(self):
        response = self.api.get(f"/star-navi/api/post/")
        assert response.status_code == 200

    def test_user_data(self):
        response = self.api.get(f"/star-navi/api/user/")
        assert response.status_code == 200

    def test_create_post(self):
        data = {
            "title": "new_title",
            "body": "new_body"
        }
        response = self.api.post(f"/star-navi/api/post/", data)
        assert response.status_code == 201
        assert response.json()['title'] == data['title']

    def test_like_post(self):
        like_response = self.api.post(f"/star-navi/api/post/{self.post.id}/like/")
        assert like_response.status_code == 200
        assert like_response.json()['status'] == 'liked'

    def test_unlike_post(self):
        Like.objects.create(user=self.user, created_at=timezone.now(),
                            content_type=ContentType.objects.get_for_model(Post),
                            object_id=self.post.id,
                            content_object=self.post)
        unlike_response = self.api.post(f"/star-navi/api/post/{self.post.id}/unlike/")
        assert unlike_response.status_code == 200
        assert unlike_response.json()['status'] == 'unliked'

    def test_analytics(self):
        Like.objects.create(user=self.user, created_at=timezone.now(),
                            content_type=ContentType.objects.get_for_model(Post),
                            object_id=self.post.id,
                            content_object=self.post)
        response_before = self.api.get(
            f"/star-navi/api/analytics/?date_from={self.one_day_ago}&date_to={self.current_date}")
        assert response_before.status_code == 200
        assert response_before.json()['count'] == 0
        response_include = self.api.get(
            f"/star-navi/api/analytics/?date_from={self.one_day_ago}&date_to={self.one_day_after}")
        assert response_include.status_code == 200
        assert response_include.json()['count'] == 1
