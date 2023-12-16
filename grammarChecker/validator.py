from rest_framework import serializers


class GrammarCheckerSerializer(serializers.Serializer):
    paragraph = serializers.CharField()

