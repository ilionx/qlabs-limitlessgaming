"""helps simply setting up a pi_cam for use"""
from cv2 import VideoCapture
from Camera.camera import Camera
from libs.decorators import deprecated


def gstreamer_pipeline(
    capture_res=(3264, 2464),  # pi cam resolution
    display=(640, 480),  # screen resolution
    framerate=21,
    flip_method=0,
):
    """
    sets up a string to enable the picam

    Parameters
    ----------
    capture_res:tuple
        int,int format
        the resolution of the captured frame
    display:tuple
        int,int format
        the resolution of the frame returned
    framerate:int
        the number of frames returned
    flip_method:int
        whether to flip the frame

    Returns
    -------
    str
        a setup string for opening a picam stream
    """
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_res[0],
            capture_res[1],
            framerate,
            flip_method,
            display[0],
            display[1],
        )
    )


@deprecated(Camera)
def cam_setup(setup=1, framerate=21):
    """
    returns a pi_cam setup

    Parameters
    ----------
    setup:int
        a integer indicating a predefined setup
    framerate:int
        the number of frames per second

    Returns
    -------
    str
        a string used to open a picam stream
    """
    if setup == 1:
        settings = gstreamer_pipeline()
    if setup == 2:
        settings = gstreamer_pipeline(
            capture_res=[1280, 720], framerate=framerate)
    else:
        settings = setup + 1
    return VideoCapture(settings)


if __name__ == "__main__":
    cam = cam_setup()
    if cam:
        print("Working!")
    else:
        print("Not Working!")
    cam.release()
