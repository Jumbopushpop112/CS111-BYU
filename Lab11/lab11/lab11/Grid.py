class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        """
            Create grid `array` width by height. Create a Grid object with
            a width, height, and array. Initially all locations hold None.
            >>> grid = Grid(2, 2)
            >>> grid.array
            [[None, None], [None, None]]
            """
        self.width = width
        self.height = height
        gridArray = [[None for x in range(width)] for y in range(height)]
        self.array = gridArray
    def in_bounds(self,x,y):
        """
          Returns True if (x, y) is in bounds
          >>> grid = Grid(3, 4)
          >>> grid.in_bounds(0, 0)
          True
          >>> grid.in_bounds(2, 3)
          True
          >>> grid.in_bounds(-1, -1)
          False
          >>> grid.in_bounds(3, 4)
          False
          """
        return (0<= x < self.width) and (0<= y < self.height)
    def get(self,x,y):
        """
            Gets the value stored value at (x, y).
            (x, y) should be in bounds.
            >>> grid = Grid(2, 2)
            >>> grid.array = [[1, 2], [4, 5]]
            >>> grid.get(0, 1)
            4
            >>> grid.get(1, 0)
            2
            """
        if self.in_bounds(x,y):
            return self.array[y][x]
        else:
            raise IndexError

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.set(1, 1, "Milk")
        >>> grid.set(1, 0, "Dud")
        >>> grid.array
        [[None, 'Dud'], [None, 'Milk']]
        """
        if self.in_bounds(x,y):
            self.array[y][x] = val
        else:
            raise IndexError
    def __str__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"
    def __repr__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"
    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.array == other.array

