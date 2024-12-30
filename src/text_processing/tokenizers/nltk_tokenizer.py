import nltk
from nltk.tokenize import word_tokenize
from typing import List
from src.text_processing.tokenizers.base_tokenizer import BaseTokenizer


class NLTKTokenizer(BaseTokenizer):
    """
    Токенизатор, использующий NLTK
    """
    def __init__(self):
        nltk.download('punkt', quiet=True)  # Download punkt tokenizer data

    def tokenize(self, text: str):
        return word_tokenize(text)
