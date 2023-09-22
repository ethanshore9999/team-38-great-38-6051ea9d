from levelup.position import Position
from levelup.map import Map

class Character:
    name = ""
    currentPosition = Position((0,0))
    map = Map()
    
    def __init__(self, character_name):
        self.name = character_name        

    def getName(self):
        return self.name
    
    def enterMap(self, map):
        self.map = map
        return 

    def getPosition(self):
     return self.currentPosition
    
    
