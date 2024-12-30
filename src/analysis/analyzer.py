from src.analysis.sentiment.simple_analyzer import SimpleAnalyzer
from src.analysis.statistics.text_stats import TextStats


class Analyzer:
    def __init__(self):
        self.sentiment_analyzer = SimpleAnalyzer()
        self.text_stats = TextStats()

    def set_sentiment_analyzer(self, sentiment_analyzer):
        self.sentiment_analyzer = sentiment_analyzer

    def analyze_sentiment(self, text):
        return self.sentiment_analyzer.analyze_sentiment(text)

    def get_text_stats(self, text):
        return self.text_stats.get_stats(text)

    def analyze_text(self, text):
        """Метод для общего анализа текста."""
        sentiment = self.analyze_sentiment(text)
        stats = self.get_text_stats(text)
        return {
            "sentiment": sentiment,
            "stats": stats
        }
