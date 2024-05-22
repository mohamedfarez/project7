import unittest
import pygame
from pygame import mixer
from unittest.mock import patch, MagicMock
from main import playsong, pausesong, stopsong, resumesong

class TestMusicPlayer(unittest.TestCase):

    @patch('pygame.mixer.music.load')
    @patch('main.playlist')
    def test_playsong(self, mock_playlist, mock_load):
        mock_playlist.get.return_value = 'song.mp3'
        playsong()
        mock_load.assert_called_with('song.mp3')
        self.assertEqual(mock_playlist.get.call_count, 1)

    @patch('pygame.mixer.music.pause')
    def test_pausesong(self, mock_pause):
        pausesong()
        mock_pause.assert_called_once()

    @patch('pygame.mixer.music.stop')
    def test_stopsong(self, mock_stop):
        stopsong()
        mock_stop.assert_called_once()

    @patch('pygame.mixer.music.unpause')
    def test_resumesong(self, mock_unpause):
        resumesong()
        mock_unpause.assert_called_once()

if __name__ == '__main__':
    unittest.main()
