from rest_framework.serializers import ModelSerializer


class ExtraSerializer(ModelSerializer):
    def image_serializer(self, obj, *args, **kwargs):
        image = getattr(obj, kwargs.get("field", "avatar"))
        try:
            image_url = image.url
        except ValueError:
            image_url = "/media/misc/image.png"
        return (
            '<div class="symbol symbol-35px me-3">'
            + f'<span class="symbol-label" style="background-image:url(/static{image_url})"></span>'
            + "</div>"
        )
