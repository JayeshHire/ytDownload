from unittest import TestCase
from ytDownload import utils
import unittest

url = "https://www.youtube.com/watch?v=A2bMuMbPq7w"
filename_audio = "love-vrindavan_song.mp3"
filename_video = "love_vrindavan_video.mp4"
filename_thumbnail = "love_vrindavan_image.png"
path_to_store = "/home/jay/source/project/api-project/media"

new_url = 'https://www.youtube.com/watch?v=AB57Z9DUREE'
new_filename_audio = "ram_naam_song.mp3"
new_filename_video = "ram_naam_video.mp4"
new_filename_thumbnail = "ram_naam_image.png"
new_path_to_store = "/home/jay/source/project/api-project/media"

class TestContentDownload( TestCase):
    instance = utils.ContentDownload(url \
                                              ,filename_audio=filename_audio\
                                                ,filename_thumbnail=filename_thumbnail \
                                                    ,filename_video=filename_video\
                                                        ,path_to_store=path_to_store) 

    def test_download_audio(self) :
        self.assertEqual(self.instance.download_audio(), 0)
        

    def test_download_video(self):
        self.assertEqual(self.instance.download_video(), 0)
        

    def test_download_thumbnail(self):
        self.assertEqual(self.instance.download_thumbnail(), 0)
        

    def test_url_setter(self):

        self.assertEqual(setattr(self.instance, url, new_url), None)
        

    def test_filename_audio_setter(self):
        self.assertEqual(setattr(self.instance, \
                                 filename_audio, new_filename_audio), None)
        

    def test_filename_video_setter(self):
        self.assertEqual(setattr(self.instance, filename_video, new_filename_video), None)
        

    def test_filename_thumbnail_setter(self):
        self.assertEqual(setattr(self.instance, \
                                 filename_thumbnail, new_filename_thumbnail), None)
        

    def test_path_to_store_setter(self):
        self.assertEqual(setattr(self.instance, path_to_store, new_path_to_store), None)
        

if __name__ == "__main__" :
    unittest.main()