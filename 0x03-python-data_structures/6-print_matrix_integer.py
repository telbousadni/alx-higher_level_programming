#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print()
    for row in matrix:
        for idx in range(len(row)):
            print("{:d}".format(row[idx]),
                  end=" " if idx + 1 < len(row) else '\n')
