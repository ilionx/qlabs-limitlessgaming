from cv2 import (COLOR_BGR2HSV, VideoCapture, cvtColor, destroyAllWindows,
                 imencode, inRange)
from numpy import array
from libs.decorators import singleton


@singleton
class Camera:
    """Simplify camera access for end users

    Attributes
    ----------
    camera: OpenCV camera object
        a camera to capture frames from
    running: bool
        a indicator for whether the camera is running
    Methods
    -------
    read(): frame
        capture a frame from the camera and return it
    show(frame)
        show a frame in a window
    """

    def __init__(self, camera=None):
        if camera is None:
            self.camera = VideoCapture(0)
        else:
            self.camera = camera

    def __del__(self):
        self.camera.release()
        destroyAllWindows()

    def read(self):
        """Read a frame from the video capture

        Returns
        -------
        list
            a frame captured from the camera
        """
        _, frame = self.camera.read()
        return frame

    def __call__(self):
        return self.read()


def to_jpg(frame):
    """Encode a raw frame to jpg format to show on a website

    Parameters
    ----------
    frame
        a frame in raw format

    Returns
    -------
    list
        a frame in jpg format
    """
    _, jpeg = imencode('.jpg', frame)
    return jpeg.tobytes()


def to_hsv(frame):
    """Turn a given frame into a HSV colored frame

    Parameters
    ----------
    frame
        a frame in raw format

    Returns
    -------
    list
        a frame in hsv format
    """
    return cvtColor(frame, COLOR_BGR2HSV)


def create_mask(frame, lower_bound, upper_bound):
    """Use the upper-and lower-bound to create a mask

    Parameters
    ----------
    frame
        the frame for which to create the mask
    lower_bound
        the lower-bound values in HSV
    upper_bound
        the upper-bound values in HSV

    Returns
    -------
    list
        a mask for the frame
    """
    return inRange(frame, array(lower_bound), array(upper_bound))


if __name__ == "__main__":
    from cv2 import __version__
    print(f"Importing open-cv: {__version__}")
