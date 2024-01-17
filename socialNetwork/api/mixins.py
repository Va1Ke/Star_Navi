from rest_framework.response import Response
from socialNetwork.models import Like
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action


class LikeModelMixin:

    @action(detail=True, methods=['post'], url_path='like')
    def liked(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if not self.has_already_liked(post, user):
            self.like(post, user)
            return Response({'status': 'liked'})
        else:
            return Response({'message': 'You already liked this'})

    @action(detail=True, methods=['post'], url_path='unlike')
    def unliked(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if self.has_already_liked(post, user):
            self.unlike(post, user)
            return Response({'status': 'unliked'})
        else:
            return Response({'message': 'You cannot unlike this'})

    def has_already_liked(self, instance, user):
        return Like.objects.filter(user=user, content_type=ContentType.objects.get_for_model(instance),
                                   object_id=instance.id).exists()

    def like(self, instance, user):
        Like.objects.create(user=user, content_object=instance)

    def unlike(self, instance, user):
        like = Like.objects.filter(user=user, content_type=ContentType.objects.get_for_model(instance),
                                   object_id=instance.id).first()
        if like:
            like.delete()
