import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from src.text_processing.lemmatizers.base_lemmatizer import BaseLemmatizer


class NLTKLemmatizer(BaseLemmatizer):
    """
    Лемматизатор, использующий NLTK
    """
    def __init__(self):
        nltk.download('wordnet', quiet=True)
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize(self, text: str):
        tokens = word_tokenize(text)
        return [self.lemmatizer.lemmatize(token) for token in tokens]
