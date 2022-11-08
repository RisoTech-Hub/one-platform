from rest_framework.serializers import ModelSerializer

from one.core.menu.models import Menu, MenuItem


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    items = MenuItemSerializer()

    class Meta:
        model = Menu
        fields = ["id", "name", "items"]
