from unittest import TestCase
from levelup.map import Map

class TestGameMap(TestCase):

    def test_get_total_positions(self):
        testObj = Map()
        results = testObj.getTotalPositions();
        assert results == 100;

    def test_get_positions(self):
        testObj = Map()
        results = testObj.getPositions();
        assert results == [0,0];  
        
    