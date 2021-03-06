import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")
        self.song_1 = Song("You\'re the best around", "Joe Esposito")
        self.song_2 = Song("Eye of the Tiger", "Survivor")
        self.song_3 = Song("Ride the Lightning", "Metallica")
        self.song_4 = Song("Paranoid", "Black Sabbath")
        

    def test_does_room_have_name(self):
        self.assertEqual("Rock Room", self.room.room_name)

    def test_has_room_got_song_list(self):
        self.assertEqual([],self.room.song_list)
    
    def test_has_room_got_guest_list(self):
        self.assertEqual([], self.room.guest_list)

    def test_can_guest_be_checked_in(self):
        guest_1 = Guest("Robute Guilliman", 500)
        guest_2 = Guest("Lion El\'Jonson", 1000000)
        room_name = Room("Rock Room")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)

        self.assertEqual(2, self.room.guest_count())
    
    def test_can_guest_be_checked_out(self):
        guest_1 = Guest("Robute Guilliman", 500)
        guest_2 = Guest("Lion El\'Jonson", 1000)
        guest_3 = Guest("Jaghatai Khan", 400)
        guest_4 = Guest("Konrad Curze", 100)
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.room.check_in_guest(guest_4)
        self.room.check_guest_out(0)

        self.assertEqual(3, self.room.guest_count())

    def test_can_song_be_added(self):
        new_song_1 = ("Just dropped in", "The First Edition")

        self.room.add_song_to_list(new_song_1)

        self.assertEqual([new_song_1], self.room.song_list)