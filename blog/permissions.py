from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorOrReadOnlyPermission(BasePermission):
    """
    Custom permission to only allow the author of a post to edit or delete it.
    Any authenticated user can create and read posts.
    """

    def has_permission(self, request, view):
        # Allow all authenticated users to create or read posts
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post.
        return obj.author == request.user
