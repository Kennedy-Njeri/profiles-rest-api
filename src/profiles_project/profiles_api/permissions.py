from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""


    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile / safe method allows you to retrieve data but not change it in the system"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id