from rest_framework.serializers import ModelSerializer


class ExtraSerializer(ModelSerializer):
    def image_serializer(self, obj, *args, **kwargs):
        image = getattr(obj, kwargs.get("field", "avatar"))
        try:
            return (
                '<div class="symbol symbol-35px me-3">'
                + f'<span class="symbol-label" style="background-image:url({image.url})"></span>'
                + "</div>"
            )
        except ValueError:
            return (
                '<div class="symbol symbol-35px me-3">'
                + '<span class="symbol-label" style="background-image:url(/static/media/misc/image.png)"></span>'
                + "</div>"
            )
