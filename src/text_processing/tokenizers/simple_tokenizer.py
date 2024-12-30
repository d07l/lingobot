from src.text_processing.tokenizers.base_tokenizer import BaseTokenizer


class SimpleTokenizer(BaseTokenizer):
    """
    Простой токенизатор
    """
    def tokenize(self, text: str):
        return text.split()
