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

    def test_detect_face_on_picture(self):
        "Test the detection of a face on a static picture"
        image = cv2.imread(ASSETS_FOLDER + self.TRUMP_PHOTO, 0)
        cascade_object = cv2.CascadeClassifier(
            self.CASCADE_FOLDER + self.FACE_CASCADE_MODEL)
        faces = []
        for i in face_recognition.find_cascade(cascade_object, image, draw=True, draw_frame=image):
            faces.append(i)
        self.assertGreaterEqual(
            len(faces), 1, "ERROR(test_detect_face_on_picture): No faces found")
    def test_detect_smile_on_picture(self):
        "Test the detection of a smile on a static picture"
        image = cv2.imread(ASSETS_FOLDER + self.TRUMP_PHOTO_SMILE, 0)
        cascade_object = cv2.CascadeClassifier(
            self.CASCADE_FOLDER + self.SMILE_CASCADE_MODEL)
        smiles = []
        for i in face_recognition.find_cascade(cascade_object, image, draw=True, draw_frame=image):
            smiles.append(i)
        self.assertGreaterEqual(
            len(smiles), 1, "ERROR(test_detect_smile_on_picture): No Smiles found")
    def test_detect_face_and_smile_on_picture(self):
        "Test the detection of a smile in a face on a static picture"
        image = cv2.imread(ASSETS_FOLDER + self.TRUMP_PHOTO_SMILE, 0)
        face_cascade_object = cv2.CascadeClassifier(
            self.CASCADE_FOLDER + self.FACE_CASCADE_MODEL)
        smile_cascade_object = cv2.CascadeClassifier(
            self.CASCADE_FOLDER + self.SMILE_CASCADE_MODEL)
        faces = []
        smiles = []
        for i in face_recognition.find_cascade(face_cascade_object, image, draw=True, draw_frame=image):
            faces.append(i)
            ROI = image[i[1]:i[1]+i[3], i[0]:i[0]+i[2]]
            ROI = ROI[len(
                ROI) // 2:]
            for j in face_recognition.find_cascade(smile_cascade_object, ROI, draw=True, draw_frame=image, start_x=i[0], start_y=i[1] + len(ROI)):
                smiles.append(j)
        self.assertGreaterEqual(
            len(faces), 1, "ERROR(test_detect_face_and_smile_on_picture): No faces found")
        self.assertGreaterEqual(
            len(smiles), 1, "ERROR(test_detect_face_and_smile_on_picture): No smiles found")
if __name__ == "__main__":
    unittest.main()
