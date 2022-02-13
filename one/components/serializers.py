from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserNestedViewSerializer(ModelSerializer):
    """
    User exclude password, username, email to update user profile
    """

    class Meta:
        model = User
        fields = (
            "id",
            "name",
        )


class FilterFieldSerializer(ModelSerializer):
    """
    Filter fields in request param
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(FilterFieldSerializer, self).__init__(*args, **kwargs)

        fields = self.context["request"].query_params.get("fields")
        if fields:
            fields = fields.split(",")
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class BaseSerializer(FilterFieldSerializer):
    """
    Base serializer
    """

    creator = UserNestedViewSerializer(read_only=True)
    last_modified_by = UserNestedViewSerializer(read_only=True)