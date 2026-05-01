#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resultrix = []
    for row in matrix:
        for i in row:
            resultrix.append(i**2)
    return resultrix
