#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sentiment_analysis.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Merilin Sousa Silva
# Matriculation Numbers: 23-726-086


import re
import nltk
from nltk.corpus import stopwords
from typing import List, Tuple, Set

nltk.download('stopwords')


def tokenize(sentences_str: str) -> List[str]:
    """Tokenize the sentences; each punctuation will become a separated token."""
    punctuation_pattern = r'([!\"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~])'
    sentences = re.sub(punctuation_pattern, r' \1 ', sentences_str)
    tokens = sentences.split()

    return tokens


def remove_stopwords(tokens: List[str]) -> List[str]:
    """Remove stopwords from the token list."""
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    return filtered_tokens


def analyse_sentiment(filtered_tokens: List[str], pos: Set[str], neg: Set[str]) -> Tuple[int, int, List[str], List[str]]:   
    """Analyze token list and count the positive and negative words"""
    # First a template list is 
    final_list = [0, 0, [], []]
    # Compare the token list with the negative and positive list and add them accordingly to the final_list
    for token in filtered_tokens:
        if token in pos:
            final_list[0] += 1
            final_list[2].append(token)
        elif token in neg:
            final_list[1] += 1
            final_list[3].append(token)
    return tuple(final_list)



def pretty_print(sentences_str, pos_counts: int, neg_counts: int, pos_words: List[str], neg_words: List[str]) -> None:
    """Print the sentiment analysis results."""
    print(sentences_str)
    print(f'\nPositive words count: {pos_counts}\tPositive words: {pos_words}')
    print(f'Negative words count: {neg_counts}\tNegative words: {neg_words}')
    if pos_counts > neg_counts:
        sentiment = 'POSITIVE'
    elif pos_counts < neg_counts:
        sentiment = 'NEGATIVE'
    else:
        sentiment = 'NEUTRAL'
    print(f'The sentiment of this quote is: {sentiment}')
    print('--'*20)


def main(): # pragma: no cover
    with open('sentiment_words/positive-words.txt', 'r') as pos_file, open('sentiment_words/negative-words.txt', 'r') as neg_file:
        pos_set = {line.strip() for line in pos_file}
        neg_set = {line.strip() for line in neg_file}
    
    with open('Good_Reads_Quotes.txt', 'r') as f:
        for line in f:
            sentences_str = line.strip()
            tokens = tokenize(sentences_str)
            filtered_tokens = remove_stopwords(tokens)
            pos_count, neg_count, pos_words, neg_words = analyse_sentiment(filtered_tokens, pos_set, neg_set)
            pretty_print(sentences_str, pos_count, neg_count, pos_words, neg_words)
    

if __name__ == '__main__': # pragma: no cover
    main()