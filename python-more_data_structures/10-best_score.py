#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns the key with the biggest integer value
    If no score is found return None"""
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
