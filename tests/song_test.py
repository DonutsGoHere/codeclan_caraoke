import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("You\'re the best around", "Joe Esposito")

    def test_has_song_got_name(self):
        self.assertEqual("You\'re the best around", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Joe Esposito", self.song.artist)

