from numpy import array
from cv2 import (CHAIN_APPROX_SIMPLE, COLOR_BGR2HSV, RETR_EXTERNAL,
                 contourArea, cvtColor, findContours, inRange)


class Scanner:
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

    def __init__(self, lower_bound=(91, 122, 138), upper_bound=(101, 255, 212)):
        self.lower_bound = array(lower_bound)
        self.upper_bound = array(upper_bound)
        self.contours = []

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
