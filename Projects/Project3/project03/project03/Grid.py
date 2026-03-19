import copy
from copy import deepcopy
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
        gridArray = [["#" for x in range(width)] for y in range(height)]
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

    @staticmethod
    def check_list_malformed(lst):
        """
        Given a list that represents a 2D nested Grid, check that it has the
        right shape. Raise a ValueError if it is malformed.
        >>> Grid.check_list_malformed([[1, 2], [4, 5]])
        >>> Grid.check_list_malformed(1)
        Traceback (most recent call last):
        ...
        ValueError: Input must be a non-empty list of lists.
        >>> Grid.check_list_malformed([[1, 2], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: All items in list must be lists of the same length.
        >>> Grid.check_list_malformed([[1, 2], 3])
        Traceback (most recent call last):
        ...
        ValueError: Input must be a list of lists.
        """
        if not isinstance(lst, list):
            raise ValueError("The object passed in is not a listed object")
        if len(lst) == 0:
            raise ValueError("The top-level list is empty!")
        for curList in lst:
            if not isinstance(curList, list):
                raise ValueError("Oops, not all the objects inside your list are lists!")
        curLength = len(lst[0])
        lst = lst[1:]
        for curList in lst:
            if not len(curList) == curLength:
                raise ValueError("Oops! Not all list elements have the same length")


    @staticmethod
    def build(lst):
        """
        Given a list that represents a 2D nested Grid construct a Grid object.
        Grid.build([[1, 2, 3], [4, 5 6]])
        >>> Grid.build([[1, 2, 3], [4, 5, 6]]).array
        [[1, 2, 3], [4, 5, 6]]
        """
        if Grid.check_list_malformed(lst):
            raise Exception("Oops, you have a malformed list!")
        gridHeight = len(lst)
        gridWidth = len(lst[0])
        myGrid = Grid(gridWidth, gridHeight)
        myGrid.array = deepcopy(lst)
        return myGrid

    def copy(self):
        """
        Return a new grid, a duplicate of the original.
        >>> grid = Grid.build([[1, 2], [4, 5]])
        >>> grid_copy = grid.copy()
        >>> grid_copy is grid
        False
        """
        return copy.deepcopy(self)
    def __eq__(self, other):
        """
        >>> grid1 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid2 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid_lst = [[1, 1, 1], [2, 3, 5]]
        >>> grid1 == grid2
        True
        >>> grid1 == grid_lst
        True
        """
        if isinstance(other, list):
            return self.array == other
        elif not isinstance(other, Grid):
            return False
        return self.array == other.array
    def __repr__(self):
        """
        >>> repr(Grid.build([[5, 5], [3, 2]]))
        'Grid.build([[5, 5], [3, 2]])'
        """
        return f"Grid.build({self.array})"