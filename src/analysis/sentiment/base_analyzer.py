from abc import ABC, abstractmethod


class BaseSentimentAnalyzer(ABC):
    """
    Абстрактный класс для анализа тональности
    """

    @abstractmethod
    def analyze_sentiment(self, text: str):
        pass
