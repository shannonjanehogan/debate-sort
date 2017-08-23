from rest_framework.permissions import BasePermission
from .models.Member import Member


class IsOwner(BasePermission):
    """Custom permission class to allow only user owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the user owner."""
        if isinstance(obj, Member):
            return obj.owner == request.user
        return obj.owner == request.user


class IsStaffOrTargetUser(BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user
