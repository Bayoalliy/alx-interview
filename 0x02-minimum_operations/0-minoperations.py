#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """calculates the fewest number of operations needed to produce
    n H characters
    """
    copied_chars = 0
    total_chars = 1
    steps = 0

    while total_chars < n:
        if n % total_chars == 0:
            copied_chars = total_chars
            steps += 1

        total_chars += copied_chars
        steps += 1

    return steps
