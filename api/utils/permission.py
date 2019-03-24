from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    message = "Vip用户专享"

    def has_permission(self, request, view):
        if request.user.type == 2:
            return True
        return False
