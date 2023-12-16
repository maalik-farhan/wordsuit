from rest_framework import serializers


class SpellCheckerSerializer(serializers.Serializer):
    paragraph = serializers.CharField()
