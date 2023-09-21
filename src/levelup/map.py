class Map:
    numPositions = 100;
    arrPositions = [0,0];
    
       
    def __init__(self):
        self.map_data = []

    def __repr__(self):
        return "Map()"

    def getTotalPositions(self):
        return self.numPositions;

    def getPositions(self):
        return self.arrPositions;