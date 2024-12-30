from src.text_processing.tokenizers.simple_tokenizer import SimpleTokenizer
from src.text_processing.stemmers.simple_stemmer import SimpleStemmer
from src.text_processing.lemmatizers.nltk_lemmatizer import NLTKLemmatizer
from src.utils.iterators import TextLineIterator, text_word_generator, WindowedTextIterator


class TextProcessor:
    def __init__(self):
        self.tokenizer = SimpleTokenizer()
        self.stemmer = SimpleStemmer()
        self.lemmatizer = NLTKLemmatizer()

    def set_tokenizer(self, tokenizer):
        self.tokenizer = tokenizer

    def set_stemmer(self, stemmer):
        self.stemmer = stemmer

    def set_lemmatizer(self, lemmatizer):
        self.lemmatizer = lemmatizer

    def tokenize(self, text, iterator_type="line"):
        """
        Токенизирует текст, используя заданный итератор
        """
        if iterator_type == "line":
            for line in TextLineIterator(text):
                for token in self.tokenizer.tokenize(line):
                    yield token
        elif iterator_type == "word":
            for word in text_word_generator(text):
                for token in self.tokenizer.tokenize(word):
                    yield token
        elif iterator_type == "window":
            for window in WindowedTextIterator(text, 10):
                for token in self.tokenizer.tokenize(window):
                    yield token

    def stem(self, text, iterator_type="line"):
        """
        Стеммирует текст, используя заданный итератор
        """
        if iterator_type == "line":
            for line in TextLineIterator(text):
                for stem in self.stemmer.stem(line):
                    yield stem
        elif iterator_type == "word":
            for word in text_word_generator(text):
                for stem in self.stemmer.stem(word):
                    yield stem
        elif iterator_type == "window":
            for window in WindowedTextIterator(text, 10):
                for stem in self.stemmer.stem(window):
                    yield stem

    def lemmatize(self, text, iterator_type="line"):
        """
        Лемматизирует текст, используя заданный итератор
        """
        if iterator_type == "line":
            for line in TextLineIterator(text):
                for lemma in self.lemmatizer.lemmatize(line):
                    yield lemma
        elif iterator_type == "word":
            for word in text_word_generator(text):
                for lemma in self.lemmatizer.lemmatize(word):
                    yield lemma
        elif iterator_type == "window":
            for window in WindowedTextIterator(text, 10):
                for lemma in self.lemmatizer.lemmatize(window):
                    yield lemma
