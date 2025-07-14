#!/usr/bin/python3
"""
factorial_recursive.py

This script calculates the factorial of a non-negative integer using recursion.
The input is taken as a command-line argument.

Usage:
    ./factorial_recursive.py <non-negative integer>
Example:
    ./factorial_recursive.py 4
    Output: 24
"""

import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input number from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
