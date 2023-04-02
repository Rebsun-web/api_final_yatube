from django.shortcuts import get_object_or_404

from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins

from posts.models import Post, Comment, Group, User
from .permissions import OwnerOrReadOnly, AuthanticatedOnly
from .serializers import (PostSerializer, CommentSerializer, UserSerializer,
                          GroupSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post, pk=post_id))


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (OwnerOrReadOnly,)


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
    permission_classes = (AuthanticatedOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
