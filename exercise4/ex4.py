# -*- coding: utf-8 -*-
from typing import List
from typing import Iterable


REPEAT_COUNT = 10


def repeat_string(text: str, repeat_count: int) -> str:
    return text * repeat_count


def remove_long_tokens(tokens: List[str], max_length: int) -> List[str]:
    # TODO: remove side effects
    new_tokens = []
    for token in tokens:
        if len(token) < max_length:
            new_tokens.append(token)
    return new_tokens


def filter_punctuation(tokens: List[str]) -> List[str]:
    # TODO: implement a function using filter() to remove punctuation
    # Hint: use string.punctuation to get a string of all punctuation characters
    return list(filter(str.isalnum, tokens))


def lowercase(tokens: str) -> List[str]:
    # TODO: implement a function using map() to lowercase the tokens
    return list(map(lambda x: x.lower(), tokens))


def length_sort(tokens: List[str]) -> List[str]:
    # TODO: improve the sorting function to sort the tokens by length
    # Hint: an anonymous function could be useful here
    return sorted(tokens, key=lambda x: len(x), reverse=True)


def uppercase(func: callable) -> callable:
    # TODO: implement a decorator to uppercase the tokens
    # the decorator should return a new function that calls the original function and then uppercases the result
    # the original function returns a list of strings
    def upper(*args, **kwargs):
        sorted_list = func(*args, **kwargs)
        return [word.upper() for word in sorted_list]
    return upper


@uppercase
def alphabetical_sort(tokens: List[str]) -> List[str]:
    # TODO: sort the tokens in alphabetical order
    return sorted(tokens)


class Alphabet:
    def __init__(self, letters: str = "abcdefghijklmnopqrstuvwxyz"):
        # Don't change this function
        self.letters = set(letters)
        self.sorted_letters = sorted(self.letters)

    # TODO: make the class iterable by implementing the __iter__ or __getitem__ method
    def __iter__(self) -> Iterable:
        return iter(self.sorted_letters)

    def __getitem__(self, index: int) -> str:
        return self.sorted_letters[index]
