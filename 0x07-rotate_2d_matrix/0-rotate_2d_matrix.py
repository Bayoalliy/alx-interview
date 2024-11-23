#!/usr/bin/python3
"""
Rotating a 2D matrix by 90 deg clockwise
"""


def rotate_2d_matrix(matrix):
    """rotates matrix"""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if j >= i:
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp

    for i in matrix:
        i.reverse()
