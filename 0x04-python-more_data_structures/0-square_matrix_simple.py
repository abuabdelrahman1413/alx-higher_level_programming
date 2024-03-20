#!/bin/python3.11
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in matrix:
        squared_matrix.append(list(map(lambda x: x ** 2, i)))
    return squared_matrix
