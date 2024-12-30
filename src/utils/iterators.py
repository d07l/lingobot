class TextLineIterator:
    """
    Итератор, который построчно читает текст из строки
    """
    def __init__(self, text: str):
        self.lines = text.splitlines()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line


def text_word_generator(text: str):
    """
    Генератор, который возвращает слова из текста
    """
    for line in TextLineIterator(text):
        for word in line.split():
            yield word


class WindowedTextIterator:
    """
    Итератор, который возвращает текст окнами заданного размера
    """
    def __init__(self, text: str, window_size: int):
        self.text = text.split()
        self.window_size = window_size
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.text):
            raise StopIteration
        end = min(self.start + self.window_size, len(self.text))
        window = " ".join(self.text[self.start:end])
        self.start += self.window_size
        return window
