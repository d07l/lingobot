from abc import ABC, abstractmethod


class BaseLemmatizer(ABC):
    """
    Абстрактный класс для лемматизаторов
    """
    @abstractmethod
    def lemmatize(self, text: str):
        pass
