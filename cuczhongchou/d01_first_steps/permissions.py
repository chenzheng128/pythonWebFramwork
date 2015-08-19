# -*- coding: utf-8 -*-

from rest_framework import permissions


"""
增加了自定义的权限类
http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
"""
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
