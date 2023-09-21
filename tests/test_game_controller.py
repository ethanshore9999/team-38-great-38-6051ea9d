from unittest import TestCase
from levelup.controller import GameController
from levelup.gamestatus import GameStatus


class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    
    def getStatus():
        testObj = GameStatus()
        assert testObj.status != None
        
