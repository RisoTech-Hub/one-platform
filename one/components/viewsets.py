from django.core.exceptions import FieldDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    """
    Custom ModelViewSet
    """

    def get_model(self):
        """return model of class"""
        return self.serializer_class.Meta.model

    def is_protected(self):
        """Check if model have is_protect field"""
        try:
            field = self.get_model()._meta.get_field("is_protected")
        except FieldDoesNotExist:
            return False
        if field.is_relation:
            return False
        return True

    @action(detail=False, methods=["delete"])
    def delete(self, request, *args, **kwargs):
        """
        Delete list
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instances = self.queryset.filter(pk__in=request.data)
        if self.is_protected():
            instances = instances.filter(is_protected=False)
        instances.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
