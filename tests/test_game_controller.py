from unittest import TestCase
from levelup.controller import GameController
from levelup.gamestatus import GameStatus
from levelup.position import Position
from levelup.map import Direction

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    
    #def test_getStatus():
     #   testObj = GameStatus()
      #  assert testObj.status != None
        
    def test_move(self):
        testObj = GameController()
        #result = testObj.move(Direction.NORTH)
        #assert testObj.status != None