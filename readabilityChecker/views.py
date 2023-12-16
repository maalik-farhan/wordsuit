# plagiarismChecker/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
import textstat
from .validator import ReadabilityCheckerSerializer
MAX_THREADS = 5


class ReadabilityCheckerView(viewsets.ViewSet):
    serializer_class = ReadabilityCheckerSerializer

    @staticmethod
    def create(request):
        serializer = ReadabilityCheckerSerializer(data=request.data)
        if serializer.is_valid():
            paragraph = serializer.validated_data['paragraph']
            spell_checker = textstat.flesch_reading_ease(paragraph)
            return Response({"readability": spell_checker}, status.HTTP_200_OK)
