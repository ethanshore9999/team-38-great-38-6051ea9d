from unittest import TestCase
from levelup.character import Character
from levelup.map import Map
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