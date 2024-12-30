from abc import ABC, abstractmethod


class BaseTokenizer(ABC):
    """
    Абстрактный класс для токенизаторов
    """
    @abstractmethod
    def tokenize(self, text: str):
        pass
