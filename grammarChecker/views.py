# grammarChecker/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .utils import grammar_check_with_replacements
from .validator import GrammarCheckerSerializer


class GrammarCheckerView(viewsets.ViewSet):
    serializer_class = GrammarCheckerSerializer

    @staticmethod
    def create(request):
        serializer = GrammarCheckerSerializer(data=request.data)
        if serializer.is_valid():
            paragraph = serializer.validated_data['paragraph']

            # Perform grammar check with replacements
            errors = grammar_check_with_replacements(paragraph)

            # Prepare the response data
            response_data = []
            for error in errors:
                error_info = {
                    'error_position': error['error_position'],
                    'error_type': error['error_type'],
                    'original_text': error['original_text'],
                    'suggestions': error['suggestions']
                }
                response_data.append(error_info)
            return Response(response_data, status.HTTP_200_OK)
