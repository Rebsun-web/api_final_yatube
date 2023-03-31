from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return request.method in permissions.SAFE_METHODS
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)


class AuthanticatedOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated)
