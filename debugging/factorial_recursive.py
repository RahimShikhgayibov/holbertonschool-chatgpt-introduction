#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using recursion. 
    It continuously multiplies the number 'n' by the factorial of 'n-1' 
    until it reaches the base case where 'n' is 0.

    Parameters:
    n (int): The non-negative integer for which the factorial is being calculated.

    Returns:
    int: The computed factorial of the provided number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Note: This will throw an error if no argument is provided or if the input is not an integer.
    f = factorial(int(sys.argv[1]))
    print(f)