from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #Allow users to edit only their own profiles, but allow everyone to view all profiles.
        if request.method in permissions.SAFE_METHODS: # GET
            return True
        
        return obj.id == request.user.id