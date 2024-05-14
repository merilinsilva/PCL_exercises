#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_sentiment_analysis.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Merilin Sousa Silva
# Matriculation Numbers: 23-726-086


import pytest
from sentiment_analysis import tokenize, remove_stopwords, analyse_sentiment, pretty_print


def test_tokenize():
    # TODO: 3 own test assertions

    # normal case
    sentence0 = "I want to sleep"
    expected0 = ['I', 'want', 'to', 'sleep']
    assert tokenize(sentence0) == expected0

    # many upper case letters and other punctuations
    sentence1 = "I AM not Happy_ for YOu!!"
    expected1 = ['I', 'AM', 'not', 'Happy', '_', 'for', 'YOu', '!', '!']
    assert tokenize(sentence1) == expected1

    # Empty string
    sentence2 = ""
    expected2 = []
    assert tokenize(sentence2) == expected2


def test_remove_stopwords():
    # TODO: 3 own test assertions
    """
    Stopwords:
    {'we', 's', 'just', 'now', 'ain', 'didn', 'have', 'in', "needn't", 'about', 'ourselves', 'any', 'from', "you'd", 'down', 'there', 'over', 'whom', 'if', 'did', 'o', "hadn't", "should've", 't', 'mightn', 'each', 'during', 'themselves', 'because', 'against', 'than', 'mustn', "haven't", 'himself', 'these', 'hadn', 'be', "that'll", 're', 'most', 'm', 'why', 'can', 'yourself', 'what', 'some', 'should', 'couldn', "shouldn't", 'do', 'had', 'shan', 'out', 'not', 'hasn', 'between', 'itself', 'through', 'above', "wouldn't", 'ours', 'been', 'other', 'again', 'very', 'needn', 'has', 'which', 'myself', 'wasn', 'isn', 'how', "weren't", 'was', 'him', 'nor', 'is', 'own', 'haven', 'below', 'doing', 'more', 'hers', 'such', 'where', "she's", 'i', 'no', 'after', "wasn't", 'on', 'so', "mustn't", 'does', 'under', 'their', 'd', 'our', 'of', "mightn't", 'at', 'but', "you'll", 'she', 'll', 'up', 'they', 'weren', 'yours', 'into', "it's", 'the', 'herself', 'are', 'for', 'will', 'won', "shan't", 'y', 'you', 'once', "won't", 'few', 'and', 'to', 'before', 'me', "hasn't", 'its', 'his', 'here', "doesn't", 'yourselves', 'until', "didn't", 'aren', 've', 'who', 'as', 'it', 'when', "aren't", 'being', 'doesn', 'shouldn', 'my', 'or', 'am', "you've", "you're", 'were', 'ma', 'with', 'only', 'don', 'her', 'this', 'those', 'having', 'an', 'while', "couldn't", "isn't", 'them', 'same', 'a', 'all', 'your', "don't", 'he', 'further', 'too', 'off', 'theirs', 'that', 'by', 'wouldn', 'then', 'both'}
    """
    # Normal case, with upper and lower case
    tokens1 = ['Just', 'want', 'tO', 'go', 'home']
    expected1 = ['want', 'go', 'home']
    assert remove_stopwords(tokens1) == expected1

    # Empty list
    tokens2 = []
    expected2 = []
    assert remove_stopwords(tokens2) == expected2

    # Only stopwords
    tokens3 = ['s', 'We', 'About']
    expected3 = []
    assert remove_stopwords(tokens3) == expected3


def test_analyse_sentiment():
    with open('sentiment_words/positive-words.txt', 'r') as pos_file, open('sentiment_words/negative-words.txt', 'r') as neg_file:
        pos_set = {line.strip() for line in pos_file}
        neg_set = {line.strip() for line in neg_file}

    # normal case
    tokens_1 = ['like', 'nonsense', ',', 'wakes', 'brain', 'cells',
                '.', 'Fantasy', 'necessary', 'ingredient', 'living', '.']
    expected_1 = (1, 1, ['like'], ['nonsense'])
    assert analyse_sentiment(tokens_1, pos_set, neg_set) == expected_1

    # empty list as input
    tokens_2 = []
    expected_2 = (0, 0, [], [])
    assert analyse_sentiment(tokens_2, pos_set, neg_set) == expected_2

    # no sentiment words in the list
    tokens_3 = ['test', 'cover', 'corner', 'cases', '!']
    expected_3 = (0, 0, [], [])
    assert analyse_sentiment(tokens_3, pos_set, neg_set) == expected_3


def test_pretty_print(capsys):
    pretty_print("Despite the rain, their picnic was filled with love and warmth, creating cherished memories.", 3, 0, [
            'love', 'warmth', 'cherished'], [])
    captured = capsys.readouterr()
    expected_output_1 = """Despite the rain, their picnic was filled with love and warmth, creating cherished memories.
\nPositive words count: 3\tPositive words: ['love', 'warmth', 'cherished']
Negative words count: 0\tNegative words: []
The sentiment of this quote is: POSITIVE
----------------------------------------
"""
    assert captured.out == expected_output_1

    pretty_print(
        "The cat slept peacefully in the afternoon sun.", 0, 0, [], [])
    captured = capsys.readouterr()
    expected_output_2 = """The cat slept peacefully in the afternoon sun.
\nPositive words count: 0\tPositive words: []
Negative words count: 0\tNegative words: []
The sentiment of this quote is: NEUTRAL
----------------------------------------
"""
    assert captured.out == expected_output_2

    pretty_print("The rain was relentless and the picnic was ruined.",
                0, 2, [], ['relentless', 'ruined'])
    captured = capsys.readouterr()
    expected_output_3 = """The rain was relentless and the picnic was ruined.
\nPositive words count: 0\tPositive words: []
Negative words count: 2\tNegative words: ['relentless', 'ruined']
The sentiment of this quote is: NEGATIVE
----------------------------------------
"""
    assert captured.out == expected_output_3
