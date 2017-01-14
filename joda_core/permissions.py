from rest_framework import permissions


class IsPublic(permissions.BasePermission):
    """Common permission which checks that content is public"""

    def has_object_permission(self, request, view, obj):
        print(obj)
        if not obj.public:
            return request.user.is_authenticated
        return True
