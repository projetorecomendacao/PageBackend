from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer


# This is here so that I can check it better later
# https://stackoverflow.com/questions/38245414/django-rest-framework-how-to-include-all-fields-and-a-related-field-in-mo
class GenericExtraFieldsSerializer(ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(GenericExtraFieldsSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
