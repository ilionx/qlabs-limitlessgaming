import numpy as np
import cv2
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))


def nothing(x):
    pass


cv2.namedWindow("trackbars")
cv2.createTrackbar("hueLow", "trackbars", 50, 179, nothing)
cv2.createTrackbar("hueHigh", "trackbars", 100, 179, nothing)

cv2.createTrackbar("saturationLow", "trackbars", 100, 255, nothing)
cv2.createTrackbar("saturationHigh", "trackbars", 255, 255, nothing)

cv2.createTrackbar("valueLow", "trackbars", 100, 255, nothing)
cv2.createTrackbar("valueHigh", "trackbars", 100, 255, nothing)

# Select an image for which you'd like to check the HSV values
camera = cv2.VideoCapture(0)
# image = cv2.imread("tests/assets/smarties.bmp")
# image = cv2.imread("tests/assets/smarties.jpg")
# image = cv2.imread("tests/assets/flower_contour.jpg")

running = True
while running:
    _, image = camera.read()
    cv2.imshow("smarties", image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hLow = cv2.getTrackbarPos("hueLow", "trackbars")
    hHigh = cv2.getTrackbarPos("hueHigh", "trackbars")
    sLow = cv2.getTrackbarPos("saturationLow", "trackbars")
    sHigh = cv2.getTrackbarPos("saturationHigh", "trackbars")
    vLow = cv2.getTrackbarPos("valueLow", "trackbars")
    vHigh = cv2.getTrackbarPos("valueHigh", "trackbars")

    lower_bound = np.array([hLow, sLow, vLow])
    upper_bound = np.array([hHigh, sHigh, vHigh])

    fourground_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    cv2.imshow("mask", fourground_mask)

    if cv2.waitKey(1) == ord('q'):
        running = False
cv2.destroyAllWindows()
camera.release()
