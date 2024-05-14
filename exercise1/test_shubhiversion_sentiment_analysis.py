import pytest
from sentiment_analysis import tokenize, remove_stopwords, analyse_sentiment, pretty_print

def test_tokenize():
    # Test sentence with punctuation
    sentence_with_punctuation = "Hello, world! How are you?"
    expected_tokens = ["Hello", ",", "world", "!", "How", "are", "you", "?"]
    assert tokenize(sentence_with_punctuation) == expected_tokens

    # Test sentence without punctuation
    sentence_without_punctuation = "This is a test sentence"
    expected_tokens = ["This", "is", "a", "test", "sentence"]
    assert tokenize(sentence_without_punctuation) == expected_tokens

    # Test empty sentence
    empty_sentence = ""
    expected_tokens = []
    assert tokenize(empty_sentence) == expected_tokens

def test_remove_stopwords():
    # Test removing stopwords
    tokens_with_stopwords = ["the", "weather", "is", "nice", "and", "it", "is", "sunny"]
    expected_tokens = ["weather", "nice", "sunny"]
    assert remove_stopwords(tokens_with_stopwords) == expected_tokens

    # Test when all tokens are stopwords
    all_stopwords = ["the", "and", "is", "it"]
    tokens = ["the", "weather", "is", "nice", "and", "it", "is", "sunny"]
    expected_tokens = ["weather", "nice", "sunny"]
    assert remove_stopwords(tokens) == expected_tokens