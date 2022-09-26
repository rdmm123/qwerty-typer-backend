from rest_framework import serializers
from apps.qwerty_core.models import Text

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text', 'lang')