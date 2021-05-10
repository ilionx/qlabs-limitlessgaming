from cv2 import (CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY, COLOR_BGR2HSV,
                 RETR_EXTERNAL, CascadeClassifier, contourArea, cvtColor,
                 findContours, inRange)
from numpy import array


class ContourScanner:
    """A scanner class for finding contours

    Attributes
    ----------
    upper_bound: array of int
        the upperBound of the contour acceptance
    lower_bound: array of int
        the lowerBound of the contour acceptance
    contours: list
        the contours found in the frame

    Methods
    -------
    find_contours(frame)
        Find contours of the given settings inside the frame
    sort_contours()
        Sort found contours based on size
    filter_contours(size=20)
        Filter the found contours based on size
    """

    def __init__(self,
                 lower_bound=(91, 122, 138),
                 upper_bound=(101, 255, 212)):
        """a contour scanner

        Parameters
        ----------
        lower_bound : tuple, optional
            the default color to search for, by default (91, 122, 138)
        upper_bound : tuple, optional
            the default color to search for, by default (101, 255, 212)
        """
        self.lower_bound = array(lower_bound)
        self.upper_bound = array(upper_bound)
        self.contours = []

    def scan(self, frame):
        self.find_contours(frame)
        self.sort_contours()
        return self.contours

    def find_contours(self, frame):
        """Find contours of the given settings inside the frame

        Parameters
        ----------
        frame
            the frame on which to find the contours
        """
        self.contours = findContours(
            self.create_mask(frame), RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)[0]

    def create_mask(self, frame):
        hsv = cvtColor(frame, COLOR_BGR2HSV)
        return inRange(hsv, self.lower_bound, self.upper_bound)

    def sort_contours(self):
        """Sort found contours based on size"""

        self.contours = sorted(self.contours,
                               key=lambda cnt: contourArea(cnt),
                               reverse=True)

    def filter_contours(self, size=20):
        """Filter the found contours based on size
        size: int
            the minimum size of contours allowed
        """
        filtered_contour_list = []
        cnt_area = True
        i = 0
        while (cnt_area) and (i < len(self.contours)):
            cnt = self.contours[i]
            area = contourArea(cnt)
            if area >= size:
                filtered_contour_list.append(cnt)
                i += 1
            else:
                cnt_area = False
        self.contours = filtered_contour_list


class CascadeScanner:
    def __init__(self, cascade_object=None, scale_factor=2.5, min_neighbors=5):
        """Create a Cascade Scanner

        Parameters
        ----------
        cascade_object : str | ClassifierObject
            a model used for object detection
        scale_factor : float
            the scale with which the image will be resized
        min_neighbors : int
            a parameter needed for the object detection
        """
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        if cascade_object is not None:
            if cascade_object is not str:
                self.cascade_object = cascade_object

            else:
                self.cascade_object = CascadeClassifier(
                    cascade_object)

    def set_cascade_object(self, cascade_object):
        if cascade_object is not str:
            self.cascade_object = cascade_object

        else:
            self.cascade_object = CascadeClassifier(
                cascade_object)

    def convert(self) -> None:
        self.frame = cvtColor(self.frame, COLOR_BGR2GRAY)

    def detect(self):
        self.objects = self.cascade_object.detectMultiScale(
            self.frame, self.scale_factor, self.min_neighbors)

    def get_objects(self):
        object_list = []
        for (x, y, width, height) in self.objects:
            object_list.append(x, y, width, height)
        return object_list

    def read_frame(self, frame):
        self.frame = frame

    def scan(self, frame=None):
        """scan a frame for a certain object

        Parameters
        ----------
        frame : ,optional
            the with the objects, by default None

        Returns
        -------
        [(int,int,int,int),...]
            the location of all the objects found in a frame
        """
        if frame is not None:
            self.frame = frame
        self.convert()
        self.detect()
        return self.get_objects()
