#!/usr/bin/python3


def print_matrix_integer(matrix=None):
    if matrix is None:
        matrix = [[]]

    for row in matrix:
        for b in range(len(row)):
            print("{:d}".format(row[b]), end="")
            if b != (len(row) - 1):
                print(" ", end="")

        print("")
