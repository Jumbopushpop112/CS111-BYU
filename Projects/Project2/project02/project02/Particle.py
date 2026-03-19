class Particle():
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y
    #return a nice formatted string
    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"
    #moving a particle function
    def physics(self):
        return None
    def move(self):
        particlePhysics = self.physics()
        if particlePhysics is None:
            return
        else:
            self.grid.set(self.x,self.y,None)
            self.x = particlePhysics[0]
            self.y = particlePhysics[1]
            self.grid.set(self.x,self.y,self)
