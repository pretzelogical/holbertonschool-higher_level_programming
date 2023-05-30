#!/usr/bin/python3
"""Custom list class"""


class MyList(list):
    """Custom list class

    Args:
        list (list): inherits the list class
    """
    def print_sorted(self):
        """Print a sorted version of the list"""
        print(sorted(self))
