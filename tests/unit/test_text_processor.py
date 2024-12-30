import pytest
from src.text_processing.text_processor import TextProcessor
from src.text_processing.tokenizers import (NltkTokenizer, SpacyTokenizer,
                                            SimpleTokenizer)
from src.text_processing.stemmers import NltkStemmer, SimpleStemmer
from src.text_processing.lemmatizers import NltkLemmatizer, SpacyLemmatizer

@pytest.fixture
def text_processor():
    return TextProcessor()

def test_text_processor_tokenize_simple(text_processor):
    text_processor.set_tokenizer(SimpleTokenizer())
    text = "This is a test."
    tokens = text_processor.tokenize(text)
    assert tokens == ["This", "is", "a", "test."]

def test_text_processor_tokenize_nltk(text_processor):
    text_processor.set_tokenizer(NltkTokenizer())
    text = "This is a test."
    tokens = text_processor.tokenize(text)
    assert tokens == ['This', 'is', 'a', 'test', '.']

def test_text_processor_tokenize_spacy(text_processor):
  text_processor.set_tokenizer(SpacyTokenizer())
  text = "This is a test."
  tokens = text_processor.tokenize(text)
  assert tokens == ["This", "is", "a", "test", "."]


def test_text_processor_stem_simple(text_processor):
    text_processor.set_stemmer(SimpleStemmer())
    text = "running runners"
    stems = text_processor.stem(text)
    assert stems == ['run', 'run']


def test_text_processor_stem_nltk(text_processor):
    text_processor.set_stemmer(NltkStemmer())
    text = "running runners"
    stems = text_processor.stem(text)
    assert stems == ['run', 'runner']

def test_text_processor_lemmatize_nltk(text_processor):
  text_processor.set_lemmatizer(NltkLemmatizer())
  text = "running runners"
  lemmas = text_processor.lemmatize(text)
  assert lemmas == ["running", "runner"]

def test_text_processor_lemmatize_spacy(text_processor):
   text_processor.set_lemmatizer(SpacyLemmatizer())
   text = "running runners"
   lemmas = text_processor.lemmatize(text)
   assert lemmas == ['run', 'runner']
