from levelup.position import Position
from levelup.controller import Direction
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
        new_x = startingPosition.position[0]
        new_y = startingPosition.position[1]
        if direction == Direction.NORTH:
            new_y += 1
        elif direction == Direction.SOUTH:
            new_y -= 1
        elif direction == Direction.WEST:
            new_x -= 1
        elif direction == Direction.EAST:
            new_x += 1  
        new_position = Positions(new_x, new_y)      
        result = isPositionValid(new_position)
        if result == True:
            return new_position
        else:
            return startingPosition

    def isPositionValid(self, positionCoordinates):
        x = positionCoordinates.position[0]
        y = positionCoordinates.position[1]
        if (x < 0 or x > 9):
            return False
        if (y < 0 or y > 9):
            return False
        return True            