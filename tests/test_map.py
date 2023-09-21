from unittest import TestCase
from levelup.map import Map

class TestMap(TestCase):

    def test_get_total_positions(self):
        testObj = Map()
        results = testObj.getTotalPositions();
        assert results == 100;

    def test_get_positions(self):
        testObj = Map()
        results = testObj.getPositions();
        #assert results == [0,0];  

    def test_calculate_position(self):
        testObj = Map()
        results = testObj.calculatePosition();
    
    def test_is_position_valid(self):
        testObj = Map()
        results = testObj.isPositionValid();

    
    
        
    