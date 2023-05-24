#!/usr/bin/python3
"""divide all elements of a matrix"""


def matrix_divided(matrix, div):
    matrix_err = "matrix must be a matrix (list of lists) of integers / floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) is not list
            or len(matrix) == 0
            or len(matrix[0]) == 0):
        raise TypeError(matrix_err)
    out_matrix = []
    row_len = len(matrix[0])
    for idx, row in enumerate(matrix):
        print(idx, row)
        if type(row) is not list:
            raise TypeError(matrix_err)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        out_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(matrix_err)
            out_row.append(round(elem/div, 2))
        out_matrix.append(out_row)
    return out_matrix
