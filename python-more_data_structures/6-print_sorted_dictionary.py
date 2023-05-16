#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by sorted keys"""
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    for key in sorted_dict.keys():
        print(f"{key}: {sorted_dict[key]}")
