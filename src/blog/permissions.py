from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthenticatedAndAuthorOnlyPermission(BasePermission):
    """
    Custom permission to only allow the author of a post to edit or delete it.
    Any authenticated user can create and read posts.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users to access any method
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read permissions only to authenticated users
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Allow write permissions (PUT, DELETE) only to the author of the post
        return obj.author == request.user
