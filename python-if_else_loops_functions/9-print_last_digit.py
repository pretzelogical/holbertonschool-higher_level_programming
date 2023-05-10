#!/usr/bin/python3
# Author: pretzelogic
# def print_last_digit(number): prints the last digit of a number


def print_last_digit(number):
    if number < 0:
        number = -number
    print(number % 10, end="")
    return number % 10
