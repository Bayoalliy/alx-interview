#!/usr/bin/python3
""" A program that solves the N queens problem """
import sys


def is_safe(queens, col):
    """checks if a queen is safe"""
    for i in range(col):
        if queens[i][1] == queens[col][1] or \
            [i, queens[col][1] + (col - i)] == queens[i] or \
                [i, queens[col][1] - (col - i)] == queens[i]:
            return False
    return True


def find_nqueen(queens, col, num):
    """recursivr function"""
    if col >= num:
        print(queens)
        return

    for i in range(num):
        queens[col][1] = i
        if is_safe(queens, col):
            find_nqueen(queens, col + 1, num)
    queens[col][1] = -1


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return(1)

    if n < 4:
        print("N must be at least 4")
        return(1)

    queens = [[i, -1] for i in range(n)]

    find_nqueen(queens, 0, n)


main()
