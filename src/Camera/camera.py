from cv2 import VideoCapture, destroyAllWindows, imencode, imshow, waitKey


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

    def __init__(self):
        self.camera = VideoCapture(0)
        self.running = True

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

    def show(self, frame):
        """Show a frame (which can be updated) in a seperate window

        Parameters
        ----------
        frame
            a frame captured from the camera
        """
        imshow("Display", frame)
        if waitKey(1) == ord("q"):  # Stop the camera if "q" is pressed
            self.running = False

    def read_jpg(self):
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
        _, jpeg = imencode('.jpg', self.read())
        return jpeg.tobytes()


if __name__ == "__main__":
    from cv2 import __version__
    print(f"Importing open-cv: {__version__}")
