from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrEditorOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if getattr(user, "role", None) == "admin":
            return True
        if getattr(user, "role", None) == "editor":
            return obj.author_id == user.id
        return False
