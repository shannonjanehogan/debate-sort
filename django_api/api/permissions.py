from rest_framework.permissions import BasePermission
from api.models.Member import Member

class IsOwner(BasePermission):
    """Custom permission class to allow only user owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the user owner."""
        if isinstance(obj, Member):
            return obj.owner == request.user
        return obj.owner == request.user
