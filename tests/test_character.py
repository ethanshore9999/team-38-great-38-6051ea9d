from unittest import TestCase
from levelup.character import Character
from levelup.map import Map
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
    
    def test_get_name(self):
        ARBITRARY_NAME = "Bobby"
        testobj = Character(ARBITRARY_NAME);
        result = testobj.getName();
        self.assertEqual(ARBITRARY_NAME, result)

    def test_enter_map(self):
        map = Map();
        ARBITRARY_NAME = "Bob";
        testobj = Character(ARBITRARY_NAME);
        testobj.enterMap(map)

    def test_getPosition(self):
        ARBITRARY_NAME = (5,5);
        testobj = Position(ARBITRARY_NAME);    
        result = testobj.getPosition()

     