#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list
    Return: Real number of elements printed"""
    printed = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed
