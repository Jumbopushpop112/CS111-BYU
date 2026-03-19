from Particle import Particle
class Sand(Particle):
    def is_move_ok(self,x,y):
        #check if a particle is in bounds first before doing any moving
        if self.grid.in_bounds(x,y):
            if (self.x == x) and (self.y+1 == y):
                if(self.grid.get(x,y) is None):
                    return True
            elif (self.x-1 == x) and (self.y+1 == y):
                if (self.grid.get(x,y) is None) and (self.grid.get(x,y-1) is None):
                    return True
            elif (self.x+1 == x) and (self.y+1 == y):
                if (self.grid.get(x,y) is None) and (self.grid.get(x,y-1) is None):
                    return True
            else:
                return False
        else:
            return False
    def physics(self):
        #check if we can move and return a tuple containing the coordinates
        if self.is_move_ok(self.x,self.y+1):
            return (self.x,self.y+1)
        elif self.is_move_ok(self.x-1,self.y+1):
            return(self.x-1,self.y+1)
        elif self.is_move_ok(self.x+1,self.y+1):
            return(self.x+1,self.y+1)
        else:
            return None

class Rock(Particle):
    def physics(self):
        return None

class Bubble(Particle):
    #acts the same as the sand class, however because we are moving up, we do the opposite operations of moving down (for example moving down is y-1 and moving up is y+1)
    def is_move_ok(self,x,y):
        if self.grid.in_bounds(x,y):
            if (self.x == x) and (self.y-1 == y):
                if(self.grid.get(x,y) is None):
                    return True
            elif (self.x+1 == x) and (self.y-1 == y):
                if (self.grid.get(x,y) is None) and (self.grid.get(x,y+1) is None):
                    return True
            elif (self.x-1 == x) and (self.y-1 == y):
                if (self.grid.get(x,y) is None) and (self.grid.get(x,y+1) is None):
                    return True
            else:
                return False
        else:
            return False
    def physics(self):
        if self.is_move_ok(self.x,self.y-1):
            return (self.x,self.y-1)
        elif self.is_move_ok(self.x+1,self.y-1):
            return(self.x+1,self.y-1)
        elif self.is_move_ok(self.x-1,self.y-1):
            return(self.x-1,self.y-1)
        else:
            return None