from math import pi, sqrt
#These functions contribute to finding the area
def squareArea(side):
    return side * side
def circleArea(radius):
    return radius * radius * pi
def areaHexagon(side):
    return ((3 * sqrt(3))/2) * (side * side)
#main function where the magic happens
def main():
    print(squareArea(4))
    print(circleArea(4))
    print(areaHexagon(4))
main()


