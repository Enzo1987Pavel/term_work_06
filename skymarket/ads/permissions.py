from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    # Право доступа для создателя объявления
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "author"):
            return request.user == obj.author
        return False


class IsAdmin(permissions.BasePermission):
    # Право доступа для администратора
    def has_permission(self, request, view):
        return request.user.role == "admin" if request.user.role else False
