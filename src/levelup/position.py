class Position:
    x_ord: int
    y_ord: int
    
    def __init__(self, xycoordinates: tuple):
        self.position:tuple = xycoordinates

   # def getPosition(self):
    #    return

    def setPosition(self,xycoordinates: tuple):
        self.position:tuple  = (x_ord, y_ord)
        return