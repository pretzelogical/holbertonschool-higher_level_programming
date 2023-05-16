#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replace all occourrences of an element by another
    in a new list"""
    out = my_list.copy()
    for i in range(len(out)):
        if out[i] == search:
            out[i] = replace
    return out
