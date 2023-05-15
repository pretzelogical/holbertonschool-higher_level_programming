#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list
    if idx is negative or
    out of range the function should
    return none
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
