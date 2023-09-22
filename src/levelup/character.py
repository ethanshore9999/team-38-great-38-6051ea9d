from levelup.position import Position


class Character:
    name = ""
    currentPosition = Position((0,0))
    
    def __init__(self, character_name):
        self.name = character_name

    def getName(self):
        return self.name
    
    def enterMap(self, map):
        return 

    def getPosition(self):
     return self.currentPosition
    
    
