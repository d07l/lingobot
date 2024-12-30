import spacy
from src.text_processing.tokenizers.base_tokenizer import BaseTokenizer


class SpacyTokenizer(BaseTokenizer):
    """
    Токенизатор, использующий spaCy
    """
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy model 'en_core_web_sm'...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def tokenize(self, text: str):
        doc = self.nlp(text)
        return [token.text for token in doc]
