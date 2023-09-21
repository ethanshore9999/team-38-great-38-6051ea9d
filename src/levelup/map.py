from levelup.position import Position
class Map:
    numPositions = 100;
    map_data = [0,0];
    #calculatePosition = [0,0];
       
    def __init__(self):
        # Creating a 2D array of CustomObject instances
        rows = 10
        cols = 10

        self.map_data = [
            [Position((i,j)) 
            for j in range(cols)] 
                for i in range(rows)
        ]
  
    def __repr__(self):
        return "Map()"

    def getTotalPositions(self):
        return self.numPositions;

    def getPositions(self):
        return self.map_data;
    
    def calculatePosition(self, startingPosition, direction):
        return self.calculatePosition;

    def isPositionValid(self, positionCoordinates):
        x = positionCoordinates.position[0]
        y = positionCoordinates.position[1]
        if (x < 0 or x > 9):
            return False
        if (y < 0 or y > 9):
            return False
        return True            