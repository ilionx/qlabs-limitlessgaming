"""Simple wrapper for using open-cv"""
import cv2
import numpy as np

from src.Camera.functions.pi_cam import cam_setup


def filter_contour(contour_list, size=20):
    """Filter a array of contours based on there area"""
    contour_list = sorted(contour_list, key=lambda x_coordinate: cv2.contourArea(
        x_coordinate), reverse=True)
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

def find_contour(frame, display_width, settings=SETTINGS, convert=True,
                 show=False, draw=False, figure="rec", color=(255, 255, 0),
                 pos=False, draw_middel=False):
    """returns all contours found in a image"""
    hue_low = settings[0]
    hue_high = settings[1]
    saturation_low = settings[2]
    saturation_high = settings[3]
    value_low = settings[4]
    value_high = settings[5]
    lower_bound = np.array([hue_low, saturation_low, value_low])
    upper_bound = np.array([hue_high, saturation_high, value_high])
    if convert:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    else:
        hsv = frame
    foreground_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    if show:
        cv2.imshow("foreground_mask", foreground_mask)
    contours, _ = cv2.findContours(
        foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x_coordinate: cv2.contourArea(
        x_coordinate), reverse=True)
    trigger = False
    return_x, return_y, _, _ = 0, 0, 0, 0
    # object_pos = (0, 0)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        (x_coordinate, y_cordinate, width, heigth) = cv2.boundingRect(cnt)
        # big contour area's are seen as objects, others are left out
        # NOTE: maybe more efficient in a while loop
        if area >= 20:
            # something went wrong, so the y_cordinate ax_coordinatele is only as long as
            # (display_width // factor) while, the x_coordinate ax_coordinatele as long as
            # the (display_height // factor)
            if y_cordinate < display_width // 2:
                trigger = True
            if draw:
                if figure == "rec":
                    cv2.rectangle(frame, (x_coordinate, y_cordinate),
                                  (x_coordinate+width, y_cordinate+heigth), color, 3)
                elif figure == "dot":
                    cv2.circle(
                        frame, (x_coordinate, y_cordinate), 2, color, -1)
            if pos and return_x == 0 and return_y == 0:
                return_x, return_y = x_coordinate + \
                    (width//2), y_cordinate + (heigth//2)
            if draw_middel:
                pass
    if pos:
        return return_x, return_y
    else:
        return trigger


def find_cascade(cascade_object, frame, scale_factor=2.5, min_neighbors=5,
                 draw=False, convert_image=False, start_x=0, start_y=0,
                 color=(255, 0, 0), draw_frame=None):
    """returns all found cascades in an image"""
    if convert_image:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade_object.detectMultiScale(
        frame, scale_factor, min_neighbors)
    for (x_coordinate, y_coordinate, width, heigth) in objects:
        if (draw and draw_frame.any()):
            cv2.rectangle(draw_frame, (start_x+x_coordinate, start_y+y_coordinate),
                          (start_x+x_coordinate+width, start_y+y_coordinate+heigth), color, 3)
        yield (x_coordinate, y_coordinate, width, heigth)


def stream(factor=2, display=[1280,960],
           cascade_folder="./cascades/", cam=2, framerate=21,
           pos=False, detect=2):
    """opens and yields a camera stream"""
    display_height = display[0]//factor
    display_width = display=1//factor
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
        passen = False
        if detect in (1, 2):
            passen = find_contour(frame, display_width, draw=True, pos=pos)
        shoot = False
        # NOTE: Finding object in gray is faster (about 3 times)
        # because it doesn't have to look for three colors (red, green, blue)
        # but only for the gray scale (0 to 255)
        if detect in (2, 3):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            for (face_x, face_y, face_w, face_h) in find_cascade(face_cascade, gray,
                                                                 draw=True, draw_frame=frame):
                # NOTE: increase accuracy and performance
                # the program checks only for smiles in the face region
                # NOTE: to reduce false positives
                # the smile is on the bottom half of the face
                # it begins on the left half side, and ends on the right half side
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
