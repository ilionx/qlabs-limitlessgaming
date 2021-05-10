"""Simple wrapper for using open-cv"""

print(
    "The functions in this file are deprecated, and should be replaced with there new variants")  # nopep8

import cv2
import numpy as np
from Camera.functions.pi_cam import cam_setup
from libs.decorators import deprecated
from Camera.scanner import CascadeScanner, ContourScanner
from Camera.camera import Camera


@deprecated(ContourScanner.filter_contours)
def filter_contour(contour_list, size=20):
    """
    Filter a array of contours based on there area

    Parameters
    ----------
    contour_list : list
        list of contours
    size : int
        minimum size of the area of the contours to be included

    Returns
    -------
    filtered_contour_list:list
        a list of contours, sorted by size, and filtered
    """
    contour_list = sorted(contour_list,
                          key=lambda x_coordinate: cv2.contourArea(
                              x_coordinate),
                          reverse=True)
    filtered_contour_list = []
    cnt_area = True
    i = 0
    while (cnt_area) and (i < len(contour_list)):
        cnt = contour_list[i]
        area = cv2.contourArea(cnt)
        if area >= size:
            filtered_contour_list.append(cnt)
            i += 1
        else:
            cnt_area = False
    return filtered_contour_list


@deprecated(ContourScanner.find_contours)
def find_contour(frame, display_width, settings=(41, 84, 40, 255, 79, 255),
                 show=False, pos=False,
                 return_all_contours=True):
    """
    Find all contours in a image

    Parameters
    ----------
    frame : list
        this is the image in which the contours must be found
    settings: tuple
        a tuple of 6 items which specify the color in HSV format.

    Returns
    -------
    contours:list
        a list of all contours found in the image
    """
    hue_low = settings[0]
    hue_high = settings[1]
    saturation_low = settings[2]
    saturation_high = settings[3]
    value_low = settings[4]
    value_high = settings[5]
    lower_bound = np.array([hue_low, saturation_low, value_low])
    upper_bound = np.array([hue_high, saturation_high, value_high])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    foreground_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    if show:
        cv2.imshow("foreground_mask", foreground_mask)
    contours: list = cv2.findContours(
        foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    if return_all_contours:
        return contours
    # TODO: Seperate function from above
    trigger = False
    return_x, return_y = 0, 0
    filtered_contour_list = filter_contour(contours)
    for cnt in filtered_contour_list:
        (x_coordinate, y_coordinate, width, height) = cv2.boundingRect(cnt)
        # something went wrong, so the y-axle is only as long as
        # (display_width // factor) while, the x-axle as long as
        # the (display_height // factor)
        if y_coordinate < display_width // 2:
            trigger = True
        if pos and return_x == 0 and return_y == 0:
            return_x, return_y = x_coordinate + \
                (width//2), y_coordinate + (height//2)
    if pos:
        return return_x, return_y
    return trigger


@deprecated(CascadeScanner.detect)
def find_cascade(cascade_object, frame, scale_factor=2.5, min_neighbors=5,
                 draw=False, convert_image=False, start_x=0, start_y=0,
                 color=(255, 0, 0), draw_frame=None):
    """
    find all cascades in an image

    Parameters
    ----------
    cascade_object:
        this is a cascade classifier which is used to find a object in
        the frame
    frame: list
        this is the image in which the object is found
    scale_factor: float
        this is a hyperparameter used by the cascade_object

    Returns
    -------
    list
        a list with all locations of the objects in the image
        in (x,y,width,height) format.
    """
    if convert_image:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade_object.detectMultiScale(
        frame, scale_factor, min_neighbors)
    for (x_coordinate, y_coordinate, width, height) in objects:
        if (draw and draw_frame.any()):
            cv2.rectangle(draw_frame,
                          (start_x+x_coordinate,
                           start_y+y_coordinate),
                          (start_x+x_coordinate+width,
                           start_y+y_coordinate+height),
                          color, 3)
        yield (x_coordinate, y_coordinate, width, height)


@deprecated(Camera.read)
def stream(factor=2, display=[1280, 960],
           cascade_folder="./cascades/", cam=2, framerate=21,
           pos=False, detect=2):
    """
    Opens and yields a camera stream

    Parameters
    ----------
    factor : int
        this is the number of times the image will be cropped before analyses.
        higher number will increase performance, but decreases the accuracy
    display: list
        this is the size of the display frame
    cascade_folder : str
        the relative locations of the folder containing the cascades
    framerate: int
        the number of frames per second captured by the camera

    Yields
    ------
    tuple
        containing filming, shoot and passen
        filming is a boolean indicating whether the camera is open
        shoot and passen are booleans indicating whether the triggers and true
    """
    display_width = display = 1//factor
    face_cascade = cv2.CascadeClassifier(
        cascade_folder+'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(
        cascade_folder+'haarcascade_smile.xml')
    shoot = False
    filming = True
    cam = cam_setup(cam, framerate=framerate)
    while filming:
        _, org_frame = cam.read()
        frame = org_frame
        if not frame:
            raise Exception(
                "Frame not found: frame is %s and expected not None" % frame)
        passen = False
        if detect in (1, 2):
            passen = find_contour(frame, display_width, draw=True, pos=pos)
        shoot = False
        # NOTE: Finding object in gray is faster (about 3 times)
        # because it doesn't have to look for three colors (red, green, blue)
        # but only for the gray scale (0 to 255)
        if detect in (2, 3):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            for (face_x, face_y, face_w, face_h) in find_cascade(
                face_cascade,
                gray,
                draw=True,
                    draw_frame=frame):
                # NOTE: increase accuracy and performance
                # the program checks only for smiles in the face region
                # NOTE: to reduce false positives
                # the smile is on the bottom half of the face
                # it begins on the left half side, and ends on the right half
                # side
                region_of_interest = gray[face_y: face_y +
                                          face_h, face_x: face_x + face_w]
                region_of_interest = region_of_interest[len(
                    region_of_interest) // 2:]
                region_of_interest_half_line = len(region_of_interest[0]) // 2
                for (smile_x, _, smile_w, _) in find_cascade(smile_cascade,
                                                             region_of_interest,
                                                             start_x=face_x,
                                                             start_y=face_y +
                                                             len(region_of_interest),
                                                             draw=1,
                                                             color=(0, 0, 255),
                                                             draw_frame=frame):
                    if (smile_x <= region_of_interest_half_line and
                            smile_x+smile_w >= region_of_interest_half_line):
                        shoot = True
        cv2.imshow('piCam', frame)
        if cv2.waitKey(1) == ord('q'):
            filming = False
        yield (filming, shoot, passen)
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    stream = stream()
