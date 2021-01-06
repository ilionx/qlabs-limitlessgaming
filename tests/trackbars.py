import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("trackbars")
cv2.createTrackbar("hueLow", "trackbars", 50, 179, nothing)
cv2.createTrackbar("hueHigh", "trackbars", 100, 179, nothing)

cv2.createTrackbar("saturationLow", "trackbars", 100, 255, nothing)
cv2.createTrackbar("saturationHigh", "trackbars", 255, 255, nothing)

cv2.createTrackbar("valueLow", "trackbars", 100, 255, nothing)
cv2.createTrackbar("valueHigh", "trackbars", 100, 255, nothing)

### Select an image for which you'de like to check the HSV values
image = cv2.imread("tests/assets/smarties.bmp")
# image = cv2.imread("tests/assets/smarties.jpg")
# image = cv2.imread("tests/assets/flower_contour.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
while True:
    cv2.imshow("smarties", image)

    hLow = cv2.getTrackbarPos("hueLow", "trackbars")
    hHigh = cv2.getTrackbarPos("hueHigh", "trackbars")
    sLow = cv2.getTrackbarPos("saturationLow", "trackbars")
    sHigh = cv2.getTrackbarPos("saturationHigh", "trackbars")
    vLow = cv2.getTrackbarPos("valueLow", "trackbars")
    vHigh = cv2.getTrackbarPos("valueHigh", "trackbars")

    lower_bound = np.array([hLow, sLow, vLow])
    upper_bound = np.array([hHigh, sHigh, vHigh])

    FGmask = cv2.inRange(hsv, lower_bound, upper_bound)
    cv2.imshow("mask", FGmask)

    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
