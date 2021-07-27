from esm_program_section.models import EditorProgram
from rest_framework.permissions import BasePermission
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from experts_section.models import Expert

# Este modelo permite a inserçãos campos da tabela relacionadao quanto tem uma relação N x N
# This is here so that I can check it better later (not used yet)
# https://stackoverflow.com/questions/38245414/django-rest-framework-how-to-include-all-fields-and-a-related-field-in-mo
class GenericExtraFieldsSerializer(ModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(GenericExtraFieldsSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class CustomModelViewSet(ModelViewSet):
    permission_classes_by_action = tuple()

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class IsExpert(BasePermission):
    def has_permission(self, request, view):
        if (request.user):
            return bool(Expert.objects.filter(email=request.user.email).exists())
        return False

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        if (request.user):
            return bool(EditorProgram.objects.filter(email=request.user.email).exists())
        return False
