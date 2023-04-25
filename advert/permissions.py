from rest_framework.permissions import BasePermission


class IsObjectAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Является ли пользователь админом (статус "superuser") (настраивается в админке)
        if request.method == "GET" or request.user.is_superuser:
            return True
        else:
            return request.user == obj.creator


