#!/usr/bin/python3

def square_value(a):
    return a * a

def square_matrix_simple(matrix=[]):
    return [[square_value(a) for a in row] for row in matrix]
