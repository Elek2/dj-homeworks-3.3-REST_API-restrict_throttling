from rest_framework.permissions import BasePermission

#  В данной программе не используется. Аналог def get_permissions(self) во views.py
class IsAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            return request.user == obj.creator



