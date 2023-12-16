from rest_framework import serializers
import nltk
import re


class PlagiarismCheckerSerializer(serializers.Serializer):
    paragraph = serializers.CharField()

    def split_sentences(self):
        processed_text = re.sub(r'(?<=[^ ])\.(?=[^ ])', '. ', self.validated_data['paragraph'])
        sentences = nltk.sent_tokenize(processed_text)
        result = [{"id": i + 1, "text": sentence} for i, sentence in enumerate(sentences)]
        return result
