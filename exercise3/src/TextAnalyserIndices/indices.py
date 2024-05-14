from abc import ABC, abstractmethod


class ReadabilityIndex(ABC):
    """
    Abstract base class for readability indices.
    """
    @abstractmethod
    def calculate(self, metrics: tuple[float, float, float]) -> float:
        pass

    @abstractmethod
    def interpret(self, index_value: float) -> str:
        pass

    def calculate_and_interpret(self, metrics: tuple[float, float, float]) -> tuple[float, str]:
        index_value = self.calculate(metrics)
        interpretation = self.interpret(index_value)
        return index_value, interpretation


class FleschKincaidGradeLevel(ReadabilityIndex):
    """
    Implementation of the Flesch-Kincaid Grade Level readability index.
    """

    def calculate(self, metrics: tuple[float, float, float]) -> float:
        avg_sentence_len, avg_syllables_per_word, _ = metrics
        index_value = round(0.39 * avg_sentence_len + 11.8 *
                            avg_syllables_per_word - 15.59, 3)
        return index_value

    def interpret(self, index_value: float) -> str:
        if index_value <= 1:
            return "Basic level for those who just learn to read books."
        elif 1 < index_value <= 5:
            return "Very easy to read."
        elif 5 < index_value <= 11:
            return "Average level. Good for the majority of marketing materials."
        else:
            return "The text is for skilled readers. For example, an academic paper."


class GunningFogIndex(ReadabilityIndex):
    """
    Implementation of the Gunning Fog Index readability index.
    """

    def calculate(self, metrics: tuple[float, float, float]) -> float:
        avg_sentence_len, _, pct_complex_words = metrics
        index_value = round(
            0.4 * (avg_sentence_len + 100 * pct_complex_words), 3)
        return index_value

    def interpret(self, index_value: float) -> str:
        if index_value <= 1:
            return "Basic level for those who just learn to read books."
        elif 1 < index_value <= 5:
            return "Very easy to read."
        elif 5 < index_value <= 8:
            return "A text is considered ideal for average readers."
        elif 8 < index_value <= 11:
            return "Fairly difficult to read."
        else:
            return "Too hard to read for the majority of readers."
