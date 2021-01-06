"""A simple testcase for the computer vision functions"""
import unittest
import cv2
import src.Camera.functions.open_face as face_recognition

ASSETS_FOLDER = "./tests/assets/"


class ComputerVisionTest(unittest.TestCase):
    """Test the Computer Vision functions"""

    CASCADE_FOLDER = "./data/models/cascades/"

    TRUMP_PHOTO = "face_trump.jpg"
    TRUMP_PHOTO_SMILE = "smile_trump.png"

    FACE_CASCADE_MODEL = "haarcascade_frontalface_default.xml"
    SMILE_CASCADE_MODEL = "haarcascade_smile.xml"

if __name__ == "__main__":
    unittest.main()
