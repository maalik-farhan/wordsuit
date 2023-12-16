from rest_framework import serializers


class ReadabilityCheckerSerializer(serializers.Serializer):
    paragraph = serializers.CharField()
