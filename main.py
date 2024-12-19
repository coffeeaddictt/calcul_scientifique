import numpy
import math

def f(x):
    return x**2 - 8 * numpy.log(x)  # Treating a list

def solve_equation(f, left, right, precision=10**(-3)):
    while right - left >= precision:
        middle = (right + left) / 2

        if f(middle) == 0:
            return middle  # Found the exact solution, return it
        elif f(left) * f(middle) < 0:  # If the solution is between left and middle
            right = middle
        elif f(right) * f(middle) < 0:  # If the solution is between middle and right
            left = middle
    
    return (right + left) / 2  # Approximation to the solution


if __name__ == "__main__":
    x = numpy.array([1, 2, 3])
    y = f(x)
    print("f(x) values for x in [1, 2, 3]:", y)
    middle = solve_equation(f, left=1, right=2)
    print("Solution (middle):", middle)
    print("f(middle):", f(middle))
