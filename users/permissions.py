from rest_framework import permissions
from .models import User

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'super admin'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'admin'

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'manager'

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'user'

class CanAssignTask(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            assigned_to_id = request.data.get('assigned_to')
            assigned_to = User.objects.get(id=assigned_to_id)
            if request.user.role.name == 'super admin':
                return True
            elif request.user.role.name == 'admin':
                return assigned_to.role.name in ['manager', 'user']
            elif request.user.role.name == 'manager':
                return assigned_to.role.name == 'user'
            return False
        return True