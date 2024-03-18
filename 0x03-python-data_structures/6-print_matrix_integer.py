#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for a in range(len(matrix[i])):
            print("{:d}".format(matrix[i][a]), end="")
            if a != (len(matrix[i]) - 1):                                                   print(" ", end="")

        print("")
