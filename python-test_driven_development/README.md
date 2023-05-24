# python test driven development

doctest:

    doctesting is named because you can achieve testing through documentation
    
    example:
        >>> print(add_integer(1, 2))
            3
    ---
        >>> print(add_integer(None))
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
