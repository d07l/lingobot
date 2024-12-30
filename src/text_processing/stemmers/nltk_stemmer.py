from nltk.stem import PorterStemmer
from src.text_processing.stemmers.base_stemmer import BaseStemmer


class NLTKStemmer(BaseStemmer):
    """
    Стеммер, использующий NLTK
    """
    def __init__(self):
        self.stemmer = PorterStemmer()

    def stem(self, text: str):
        return [self.stemmer.stem(word) for word in text.split()]
