import unittest


import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")

    def test_does_room_have_name(self):
        self.assertEqual("Rock Room", self.room.room_name)

    def test_has_room_got_song_list(self):
        self.assertEqual([], self.room.song_list)
    
    def test_has_room_got_guest_list(self):
        self.assertEqual([], self.room.guest_list)