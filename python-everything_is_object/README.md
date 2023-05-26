# python everything is object

# Interning
Python uses a technique called interning for immutable objects, such as integers. Interning means that when you create a new immutable object with a value that already exists, Python will reuse the existing object instead of creating a new one. This is done to conserve memory.

>>> a = 89
>>> b = 89
>>> id(a)
140737488348040
>>> id(b)
140737488348040

