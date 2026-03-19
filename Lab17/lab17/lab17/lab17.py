def load_grid(filename):
    """YOUR CODE HERE"""
    listCharacters = []
    with open(filename,"r") as file:
        for line in file:
            listLine = []
            line = line.strip("\n")
            for character in line:
                listLine.append(character)
            listCharacters.append(listLine)
    return listCharacters

def exists(grid, word):
    visited = []
    def in_bounds(i,j):
        return i>=0 and i<len(grid) and j>=0 and j<len(grid[0])
    def helper(i,j,wordi):
        if wordi == len(word):
            return True
        if not in_bounds(i,j) or (i,j) in visited or grid[i][j] != word[wordi]:
            return False
        visited.append((i,j))
        for di,dj in ((i+1,j), (i,j+1), (i-1,j), (i,j-1)):
            if helper(di,dj, wordi+1):
                return True
        return False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                if helper(i,j,0):
                    visited = []
                    return True
    return False