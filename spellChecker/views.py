# plagiarismChecker/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
import concurrent.futures
from functools import partial
from .utils import CustomSpellChecker
from .validator import SpellCheckerSerializer
MAX_THREADS = 5


class SpellCheckerView(viewsets.ViewSet):
    serializer_class = SpellCheckerSerializer

    @staticmethod
    def create(request):
        serializer = SpellCheckerSerializer(data=request.data)
        if serializer.is_valid():
            paragraph = serializer.validated_data['paragraph']
            spell_checker = CustomSpellChecker()
            suggestions = spell_checker.check_spelling(paragraph)
            end_res = []
            for word, suggestion_list in suggestions.items():
                end_res.append({"Word": word, "Suggestions": suggestion_list})
            return Response(end_res, status.HTTP_200_OK)
