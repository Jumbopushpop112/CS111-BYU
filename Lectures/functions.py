# generalizing for a value: r
from math import pi, sqrt

def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    if r < 0:
        return 0
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)
def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)
def f(x):
    return g(x-1)
def g(y):
    return abs(h(y)- h(1/y))
def h(z):
    return z * z
computed_area = area_square(2)
print(f'area of square = {computed_area:.2f}')
computed_area = area_circle(3)
print(f'area of circle = {computed_area:.2f}')
computed_area = area_hexagon(4)
print(f'area of hexagon = {computed_area:.2f}')
