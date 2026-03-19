from Grid import *
import sys
import random
def main():
    #validating commands
    try:
        if sys.argv[1] == "-s":
            if len(sys.argv) < 3:
                print("Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]")
            else:
                solveMaze(sys.argv[2])
        #time for us to generate a maze
        elif sys.argv[1] == "-g":
            if len(sys.argv) < 5:
                print("Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]")
            else:
                width = int(sys.argv[2])
                height = int(sys.argv[3])
                filename = sys.argv[4]
                generateMaze(width,height,filename)
    #catching exceptions
    except Exception as e:
        print(f"An error occured: {e}")
#load the grid in
def load_grid(filename):
    listCharacters = []
    with open(filename,"r") as file:
        for line in file:
            listLine = []
            line = line.strip("\n")
            for character in line:
                listLine.append(character)
            listCharacters.append(listLine)
    return listCharacters
#find starting point
def findStartingPoint(maze):
    for y in range(maze.height):
        for x in range(maze.width):
            if maze.get(x,y) == "S":
                return(x,y)
#help us get out of here
def mazeHelper(x,y,maze):
    if maze.get(x,y) == "E":
        return True
    elif maze.get(x,y) in ["#","."]:
        return False
    maze.set(x,y,".")
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        newX = dx + x
        newY = dy + y
        if maze.in_bounds(newX,newY):
            if mazeHelper(newX, newY, maze):
                return True
    maze.set(x,y," ")
    maze.set(1, 1, "S")
    return False
def solveMaze(filename):
    maze = Grid.build(load_grid(filename))
    startingPoint = findStartingPoint(maze)
    x = startingPoint[0]
    y = startingPoint[1]
    if mazeHelper(x,y,maze):
        print("Success! The path is as follows:")
        for y in range(maze.height):
            for x in range(maze.width):
                print(maze.get(x,y),end="")
            print()
    else:
        print("Error!  Solver could find no solution to the maze.")
def generateMaze(width, height, filename):
    def helper(maze,x,y):
        #EWSN
        directions = [(2,0),(-2,0),(0,2),(0,-2)]
        random.shuffle(directions)
        for direction in directions:
            newX = x + direction[0]
            newY = y + direction[1]
            if maze.in_bounds(newX,newY) and maze.get(newX,newY) == "#":
                intermediateX = x + (direction[0]//2)
                intermediateY = y + (direction[1]//2)
                maze.set(intermediateX,intermediateY," ")
                maze.set(newX,newY," ")
                helper(maze,newX,newY)
    if width < 3 or height < 5:
        print('Error! Minimum maze size is 3x5! Check your dimensions again.')
        return
    if width % 2 == 0:
       width += 1
    if height % 2 == 0:
       height += 1
    maze = Grid(width,height)
    maze.set(1,1,"S")
    helper(maze,1,1)
    maze.set(maze.width-2,maze.height-2,"E")
    writeMaze(maze,filename)
def writeMaze(maze, filename):
    with open(filename,"w") as file:
        for y in range(maze.height):
            for x in range(maze.width):
                file.write(maze.get(x,y))
            file.write("\n")
main()