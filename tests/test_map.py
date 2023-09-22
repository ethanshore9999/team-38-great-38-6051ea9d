# This file accommodates testing of map.py, including initialization
# while testing placing the char on opposite corners of the map,
# getting the position, getting total positions....

from unittest import TestCase
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    def test_init(self):
        testObj = Map()
        assert testObj.map_data[0][0].position == (0,0)
        assert testObj.map_data[9][9].position == (9,9)

    def test_get_total_positions(self):
        testObj = Map()
        results = testObj.getTotalPositions();
        assert results == 100;

    def test_get_positions(self):
        testObj = Map()
        assert testObj.getPositions()[0][0].position == (0,0)
  
    def test_calculate_position(self):
        testObj = Map()
        #results = testObj.calculatePosition();
    
    def test_is_position_valid(self):
        testObj = Map()
        results = testObj.isPositionValid(Position((1,1)));
        assert results == True
    
    def test_is_position_validy(self):
        testObj = Map()
        results = testObj.isPositionValid(Position((1,10)));
        assert results == False
        
    