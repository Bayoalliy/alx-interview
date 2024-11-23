#!/usr/bin/python3
"""
Rotating a 2D matrix by 90 deg clockwise
"""


def rotate(matrix, col, x, start_idx):
    """rotates at a single index"""
    r = start_idx
    c = col
    end_idx = (len(matrix) - 1) - start_idx
    size = end_idx - start_idx

    for i in range(size * x):
        if c < end_idx and r == start_idx:
            c += 1
        elif c == end_idx and r < end_idx:
            r += 1
        elif r == end_idx and c > start_idx:
            c -= 1
        elif c == start_idx and r > start_idx:
            r -= 1

    tmp = matrix[r][c]
    matrix[r][c] = matrix[start_idx][col]
    matrix[start_idx][col] = tmp


def rotate_mtx(matrix, size, a):
    """recursively rotates sub-matrix"""
    if size < 2:
        return
    n = len(matrix) - (a + 1)
    for j in range(a, n):
        for i in range(1, 4):
            rotate(matrix, j, i, a)

    rotate_mtx(matrix, size - 2, a + 1)


def rotate_2d_matrix(matrix):
    """main funcction"""
    rotate_mtx(matrix, len(matrix), 0)
