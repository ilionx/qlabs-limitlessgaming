"""A simple testcase for the audio model classifier"""
import os
import sys
sys.path.insert(0, os.path.abspath('./src'))

import unittest
import cv2
import Camera.functions.open_face as face_recognition
import time

ASSETS_FOLDER = "./tests/assets/"
CASCADE_FOLDER = "./data/models/cascades/"
FACE_CASCADE_MODEL = "haarcascade_frontalface_default.xml"
SMILE_CASCADE_MODEL = "haarcascade_smile.xml"
THRESHOLD = 0.500
AMOUNT = 100  # takes about 14 seconds to complete all 4 tests


class PerformanceTest(unittest.TestCase):
    """Test the performance of the used functions"""
    @staticmethod
    def calculate_average_time(start, end, amount):
        """return the average time between start and end"""
        delta = end - start
        average_time = delta / amount
        return average_time

    def test_load_image(self):  # average = 0.02 seconds
        """load an image 100 times, and calculate the average loading time"""
        path_to_image = "face_trump.jpg"

        start = time.time()
        for _ in range(AMOUNT):
            image = cv2.imread(ASSETS_FOLDER + path_to_image)
        end = time.time()

        average_time = PerformanceTest.calculate_average_time(
            start, end, AMOUNT)
        self.assertLessEqual(average_time, THRESHOLD,
                             "The average time was %f seconds, but needed to be at least %f seconds" % (average_time, THRESHOLD))

    def test_process_images_cascade(self):  # average = 0.05 seconds
        """execute face recognition on a 100 images, and calculate the average processing time"""
        path_to_image = "face_trump.jpg"
        # preparation
        cascade_object = cv2.CascadeClassifier(
            CASCADE_FOLDER + FACE_CASCADE_MODEL)
        faces = []

        start = time.time()
        for _ in range(AMOUNT):
            image = cv2.imread(ASSETS_FOLDER + path_to_image, 0)
            for i in face_recognition.find_cascade(cascade_object, image, draw=True, draw_frame=image):
                faces.append(i)
        end = time.time()

        average_time = PerformanceTest.calculate_average_time(
            start, end, AMOUNT)
        self.assertLessEqual(
            average_time, THRESHOLD, "The average time was %f seconds, but needed to be at least %f seconds" % (average_time, THRESHOLD))

    def test_process_images_contour(self):  # average = 0.007 seconds
        """process the contour of 100 images, and calculate the average processing time"""
        path_to_image = "flower_contour_crop.jpg"
        # preparation
        SETTINGS = (19, 35, 225, 255, 82, 255)

        start = time.time()
        for _ in range(AMOUNT):
            image = cv2.imread(ASSETS_FOLDER + path_to_image)
            contours = face_recognition.find_contour(
                image, 2, pos=True, settings=SETTINGS, return_all_contours=True)
            filtered_contour_list = face_recognition.filter_contour(contours)
        end = time.time()

        average_time = PerformanceTest.calculate_average_time(
            start, end, AMOUNT)
        self.assertLessEqual(
            average_time, THRESHOLD, "The average time was %f seconds, but needed to be at least %f seconds" % (average_time, THRESHOLD))

    def test_process_images_both(self):  # average = 0.06 seconds
        """process face recognition and the contours of 100 images, and calculate the average processing time"""
        path_to_image_contour = "flower_contour_crop.jpg"
        path_to_image_cascade = "face_trump.jpg"
        # preparation
        SETTINGS = (19, 35, 225, 255, 82, 255)
        cascade_object = cv2.CascadeClassifier(
            CASCADE_FOLDER + FACE_CASCADE_MODEL)
        faces = []

        start = time.time()
        for _ in range(AMOUNT):
            image = cv2.imread(ASSETS_FOLDER + path_to_image_contour)
            contours = face_recognition.find_contour(
                image, 2, pos=True, settings=SETTINGS, return_all_contours=True)
            filtered_contour_list = face_recognition.filter_contour(contours)
            image = cv2.imread(ASSETS_FOLDER + path_to_image_cascade, 0)
            for i in face_recognition.find_cascade(cascade_object, image, draw=True, draw_frame=image):
                faces.append(i)
        end = time.time()

        average_time = PerformanceTest.calculate_average_time(
            start, end, AMOUNT)
        self.assertLessEqual(
            average_time, THRESHOLD, "The average time was %f seconds, but needed to be at least %f seconds" % (average_time, THRESHOLD))


if __name__ == "__main__":
    unittest.main()
