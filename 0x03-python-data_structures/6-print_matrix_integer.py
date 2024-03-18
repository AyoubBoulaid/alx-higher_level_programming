#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for b in range(len(matrix)):
        for a in range(len(matrix[b])):
            print("{:d}".format(matrix[b][a]), end="")
            if a != (len(matrix[b]) - 1):                                                   print(" ", end="")
        print("")
