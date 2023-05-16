#!/usr/bin/python3


def quick_sort(arr):
    """Quick sort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    sorted = quick_sort(my_list)
    return sorted[-1]
