#!/usr/bin/python3

def add_args(args, len):

    sum = 0
    if len > 1:
        for i in range(1, len):
            sum += int(args[i])
    return sum


if __name__ == "__main__":
    import sys

    argv = sys.argv
    print(add_args(argv, len(argv)))
