# This file accommodates testing of map.py, including initialization
# while testing placing the char on opposite corners of the map,
# getting the position, getting total positions....

from unittest import TestCase
from levelup.map import Map
from levelup.position import Position
from levelup.map import Direction

class TestMap(TestCase):
    bottomLeftBoundary = (0,0)
    topRighttBoundary = (9,9)
    def test_init(self):
        testObj = Map()
        assert testObj.map_data[0][0].position == self.bottomLeftBoundary
        assert testObj.map_data[9][9].position == self.topRighttBoundary

    def test_get_total_positions(self):
        testObj = Map()
        results = testObj.getTotalPositions();
        assert results == 100;

    def test_get_positions(self):
        testObj = Map()
        assert testObj.getPositions()[0][0].position == self.bottomLeftBoundary
        assert testObj.getPositions()[9][9].position == self.topRighttBoundary

    def test_calculate_position(self):
        testObj = Map()
        currentPosition =  Position((1,1))
        results = testObj.calculatePosition(currentPosition,Direction.NORTH);
        assert results.position == (1,2)

    def test_calculate_position_fail(self):
        testObj = Map()
        currentPosition =  Position((1,2))
        results = testObj.calculatePosition(currentPosition,Direction.NORTH);
        assert results.position == (1,3)
    
    def test_position_inBounds(self):
        testObj = Map()
        results = testObj.isPositionValid(Position((1,1)));
        assert results == True
    
    def test_position_outOfBounds(self):
        testObj = Map()
        results = testObj.isPositionValid(Position((1,10)));
        results = testObj.isPositionValid(Position((10,1)));
        results = testObj.isPositionValid(Position((-1,5)));
        results = testObj.isPositionValid(Position((5,-1)));
        assert results == False
        
