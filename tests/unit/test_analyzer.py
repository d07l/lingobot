import pytest
from src.analysis.analyzer import Analyzer
from src.analysis.sentiment.simple_analyzer import SimpleAnalyzer
from src.analysis.sentiment.vader_analyzer import VaderAnalyzer

@pytest.fixture
def analyzer():
    return Analyzer()

def test_analyzer_analyze_sentiment_vader(analyzer):
  analyzer.set_sentiment_analyzer(VaderAnalyzer())
  text = "This is a great movie!"
  sentiment = analyzer.analyze_sentiment(text)
  assert sentiment['compound'] > 0.5

def test_analyzer_analyze_sentiment_simple(analyzer):
    analyzer.set_sentiment_analyzer(SimpleAnalyzer())
    text = "good"
    sentiment = analyzer.analyze_sentiment(text)
    assert sentiment == "Positive"

def test_analyzer_get_text_stats(analyzer):
    text = "This is a test string."
    stats = analyzer.get_text_stats(text)
    assert stats['word_count'] == 5
    assert stats['avg_word_length'] == 3.0
    assert stats['sentence_count'] == 1
