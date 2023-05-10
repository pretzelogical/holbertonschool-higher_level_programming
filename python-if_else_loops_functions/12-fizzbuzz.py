#!/usr/bin/python3
# Author: pretzelogic
# def fizzbuzz(): prints the numbers 1 to 100 
# if a number is a multiple of 3 print Fizz
# if a number is a multiple of 5 print Buzz
# if number is a multiple of both 3 & 5 print FizzBuzz
def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

