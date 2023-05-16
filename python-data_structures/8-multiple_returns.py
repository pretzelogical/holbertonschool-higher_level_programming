#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string
    and its first character
    If sentence is empty the first character is none"""
    if sentence == "":
        return 0, None
    return len(sentence), sentence[0]
