from abc import ABC, abstractmethod

class BaseStemmer(ABC):
    """
    Абстрактный класс для стеммеров
    """
    @abstractmethod
    def stem(self, text: str):
        pass
