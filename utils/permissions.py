
from rest_framework import permissions


class IsOwnerUserOrReadOnly(permissions.BasePermission):
    """Custom permissions."""

    def has_object_permission(self, request, view, instance):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == instance.id


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """Custom permissions."""

    def has_object_permission(self, request, view, instance):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permissions."""

    def has_object_permission(self, request, view, instance):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == instance.user.id


class IsAdminORReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff