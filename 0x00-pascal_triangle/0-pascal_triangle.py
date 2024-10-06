#!/usr/bin/python3

"""
function that creates a pascal triangle
"""


def pascal_triangle(n):
    """ pascal triangle function """

    triangle = []

    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            last_row = triangle[-1]

            idx = 0
            new_row = []

            for num in last_row:
                if idx == 0:
                    new_row.append(1)

                else:
                    new_row.append(num + last_row[idx - 1])
                if idx == len(last_row) - 1:
                    new_row.append(1)
                idx += 1
            triangle.append(new_row)
    return (triangle)
