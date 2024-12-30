import spacy
from src.text_processing.lemmatizers.base_lemmatizer import BaseLemmatizer


class SpacyLemmatizer(BaseLemmatizer):
    """
    Лемматизатор, использующий spaCy
    """
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy model 'en_core_web_sm'...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def lemmatize(self, text: str):
        doc = self.nlp(text)
        return [token.lemma_ for token in doc]
