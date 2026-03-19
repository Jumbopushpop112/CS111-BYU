from Grid import Grid
import random
"""*** BEGIN PROVIDED CODE ***"""
def print_grid(grid):
    """
    Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()
"""*** END PROVIDED CODE ***"""


def random_rocks(grid, chance_of_rock):
    """
    Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    """*** YOUR CODE HERE ***"""
    copyGrid = Grid.copy(grid)
    for y in range(copyGrid.height):
        for x in range(copyGrid.width):
            if copyGrid.get(x,y) is None:
             randomNum = random.random()
             if randomNum <= chance_of_rock:
                copyGrid.array[y][x] = "r"
    return copyGrid




def random_bubbles(grid, chance_of_bubbles):
    """
    Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    """*** YOUR CODE HERE ***"""
    copyGrid = Grid.copy(grid)
    for y in range(copyGrid.height):
        for x in range(copyGrid.width):
            if copyGrid.get(x, y) is None:
                randomNum = random.random()
                if randomNum <= chance_of_bubbles:
                    copyGrid.array[y][x] = "b"
    return copyGrid

def modify_grid(grid, char, prob):
    """
    Write a function which can take in a grid, a single character
    and a probability as parameters and updates the grid using
    the character passed in.
    """
    """*** YOUR CODE HERE ***"""
    copyGrid = Grid.copy(grid)
    for y in range(copyGrid.height):
        for x in range(copyGrid.width):
          if copyGrid.get(x, y) is None:
            randomNum = random.random()
            if randomNum <= prob:
                copyGrid.array[y][x] = char
    return copyGrid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    """*** YOUR CODE HERE ***"""
    copyGrid = Grid.copy(grid)
    if copyGrid.get(x,y-1) is None:
        copyGrid.array[y-1][x] = "b"
        copyGrid.array[y][x] = None
    return copyGrid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    """*** YOUR CODE HERE ***"""
    copyGrid = Grid.copy(grid)
    for y in range(copyGrid.height):
        for x in range(copyGrid.width):
            if copyGrid.get(x,y) == "b":
                if y == 0:
                    continue
                elif copyGrid.get(x,y-1) is None:
                    copyGrid = bubble_up(copyGrid,x,y)
    return copyGrid

"""*** BEGIN PROVIDED CODE ***"""
def animate_grid(grid, delay):
    """
    Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1
"""*** END PROVIDED CODE ***"""
