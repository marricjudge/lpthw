from nose.tools import *
from ex47.game import Room

def test_room():
    test = Room("Roomtester")
    assert_equal(test.name, "Roomtester")
    assert_equal(test.paths, {})

def test_room_paths():
    center = Room("Center")
    north = Room("North")
    south = Room("South")

    center.add_paths({"north": north, "south" : south})

    assert_equal(center.go("north"), north)
    assert_equal(center.go("south"), south)

def test_map():
    start = Room("Start")
    west = Room ("Trees")
    down = Room("Dungeon")

    start.add_paths({"west":west, "down": down})
    west.add_paths({"east": start})
    down.add_paths({"up": start})

    assert_equal.start.go({"west":werst, "down": down})
