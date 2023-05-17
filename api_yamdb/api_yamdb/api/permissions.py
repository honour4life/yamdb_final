from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.role == 'admin')


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.user == obj
                or request.user == obj.author)


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == 'moderator')


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == 'admin')


class IsOwnerModeratorAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and (request.user == obj
                     or request.user == obj.author
                     or request.user.role == 'moderator'
                     or request.user.role == 'admin'))


class IsAnyRoleOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj
                or request.user == obj.author
                or request.user.role == 'moderator'
                or request.user.role == 'admin')


class IsOwnerAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and (request.user == obj
                     or request.user == obj.author
                     or request.user.role == 'admin'))


class IsModeratorAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.role == 'moderator'
                     or request.user.role == 'admin'))
