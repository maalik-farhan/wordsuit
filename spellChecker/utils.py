from spellchecker import SpellChecker as PySpellChecker  # Alias the class


class CustomSpellChecker:
    def __init__(self, language='en'):
        self.spell = PySpellChecker(language=language)

    def check_spelling(self, text):
        words = text.split()
        misspelled = self.spell.unknown(words)

        suggestions = {}
        for word in misspelled:
            suggestions[word] = self.spell.candidates(word)

        return suggestions
