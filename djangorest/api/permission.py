from rest_framework.permissions import BasePermission
from .models import Bucketlist

class IsOwner(BasePermission):
    """Custom Permission class to allow only bucketlist owners to edit them"""

    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted"""
        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user



    # The class above implements a permission which holds by this truth
    #  – The user has to be the owner to have that object's
    # permission. If they are indeed the owner of that bucketlist,
    # it returns True, else False.