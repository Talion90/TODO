from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    message = "You must be a author of the task"

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsAuthorOrExecutor(BasePermission):

    message = "You must be a author or executor of the task"

    def has_object_permission(self, request, view, obj):
        if obj.task.author == request.user or any(User.objects.get(id=executor['id']).id == request.user.id
                                                  for executor in list(obj.task.executors.values())):
            return True
        return False
