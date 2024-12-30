from src.text_processing.stemmers.base_stemmer import BaseStemmer


class SimpleStemmer(BaseStemmer):
    """
    Простой стеммер (удаляет окончания
    """
    def stem(self, text):
        tokens = text.split()
        return [token[:-3] if len(token) > 3 else token for token in tokens]
