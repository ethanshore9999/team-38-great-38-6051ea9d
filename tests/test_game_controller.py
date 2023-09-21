from unittest import TestCase
from levelup.controller import GameController
from levelup.gamestatus import GameStatus
from levelup.position import Position

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    
    #def test_getStatus():
     #   testObj = GameStatus()
      #  assert testObj.status != None
        
    def test_move(self):
        testObj = GameController()
        result = testObj.move('N')
        assert testObj.status != None