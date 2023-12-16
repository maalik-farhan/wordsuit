# plagiarismChecker/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
import concurrent.futures
from functools import partial
from .validator import PlagiarismCheckerSerializer
from .utils import scrape, scrape_and_check
MAX_THREADS = 5


class PlagiarismCheckerView(viewsets.ViewSet):
    serializer_class = PlagiarismCheckerSerializer

    @staticmethod
    def create(request):
        serializer = PlagiarismCheckerSerializer(data=request.data)
        if serializer.is_valid():
            userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
            paragraph = serializer.split_sentences()
            end_res = []

            # Define context_data and response_cache inside the function
            context_data = {}
            response_cache = {}

            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                res = executor.map(scrape, paragraph, [userAgent] * len(paragraph))

            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                executor.map(partial(scrape_and_check, user_agent=userAgent, context_data=context_data, response_cache=response_cache), res)

            for context in context_data:
                end_res.append(context_data[context])

            return Response(end_res, status.HTTP_200_OK)
