from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class User(AbstractUser):
    last_time_request = models.DateTimeField(null=True, blank=True)


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_like', fields=['user', 'content_type', 'object_id'])
        ]


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(max_length=255, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    likes = GenericRelation(Like, related_query_name='post_likes')

    @property
    def likes_count(self):
        return Like.objects.filter(content_type=ContentType.objects.get_for_model(self),
                                   object_id=self.id).count()
