class Map:
    numPositions = 100;
       
    def __init__(self):
        self.map_data = []

    def __repr__(self):
        return "Map()"

    def getTotalPositions(self):
        return self.numPositions;