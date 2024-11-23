#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 7, 7, 2],
              [4, 5, 6, 2, 5, 1],
              [7, 8, 9, 6, 7, 2],
              [6, 3, 8, 1, 6, 8],
              [7, 8, 9, 6, 7, 2],
              [6, 3, 8, 1, 6, 8]]

    mtx = [[1, 2], [3, 4]]
    rotate_2d_matrix(mtx)
    print(mtx)
    rotate_2d_matrix(matrix)
    print(matrix)
