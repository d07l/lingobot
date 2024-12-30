class TextStats:
    def get_stats(self, text):
        """
        Считает базовые статистические данные по тексту
        """
        words = text.split()
        word_count = len(words)
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        avg_word_length = 0
        if word_count > 0:
            avg_word_length = sum(len(word) for word in words) / word_count

        return {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "avg_word_length": avg_word_length
        }
