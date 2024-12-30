from src.analysis.sentiment.base_analyzer import BaseSentimentAnalyzer


class SimpleAnalyzer(BaseSentimentAnalyzer):
    """
    Простой анализатор тональности
    """

    def analyze_sentiment(self, text):
        """
        Анализирует тональность текста простым способом
        """
        #  простая реализация, в которой смотрим на количество позитивных и негативных слов
        positive_words = ["happy", "good", "great", "amazing", "excellent"]
        negative_words = ["bad", "terrible", "awful", "poor", "disappointing"]
        text = text.lower()
        positive_count = sum([1 for word in positive_words if word in text])
        negative_count = sum([1 for word in negative_words if word in text])
        total = positive_count+negative_count

        if total == 0:
            return {"positive": 0, "negative": 0, "neutral": 1}

        return {
            "positive": positive_count/total,
            "negative": negative_count/total,
            "neutral": (total - positive_count-negative_count)/total
        }
