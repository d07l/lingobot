import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.analysis.sentiment.base_analyzer import BaseSentimentAnalyzer


class VaderAnalyzer(BaseSentimentAnalyzer):
    """
    Анализатор тональности, использующий VADER
    """
    def __init__(self):
        nltk.download('vader_lexicon', quiet=True)
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text: str):
        scores = self.analyzer.polarity_scores(text)
        return scores['compound']
