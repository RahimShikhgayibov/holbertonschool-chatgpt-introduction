#!/usr/bin/python3
import sys

def factorial(n):
    # Handle negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    result = 1
    while n > 1:
        result *= n
        n -= 1  # CRITICAL FIX: Decrement n to avoid an infinite loop
    return result

# Ensure the script is being run directly
if __name__ == "__main__":
    # Check if the user provided an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
        
    try:
        # Attempt to convert the argument to an integer and calculate
        number = int(sys.argv[1])
        f = factorial(number)
        print(f)
    except ValueError as e:
        # Handle cases where the input isn't a valid integer or is negative
        print(f"Error: Invalid input. Please provide a valid non-negative integer.")