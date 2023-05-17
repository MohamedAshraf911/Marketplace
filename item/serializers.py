from rest_framework import serializers
from .models import Category, Item


class Dserializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','description']#"__all__"
