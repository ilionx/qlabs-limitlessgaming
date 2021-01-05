"""helps simply setting up a pi_cam for use"""
from cv2 import VideoCapture

def gstreamer_pipeline(
    capture_res=(3264, 2464),  # pi cam resolution
    display=(640, 480),  # screen resolution
    framerate=21,
    flip_method=0,
):
    """sets up a string to enable the picam"""
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


def cam_setup(setup=1, framerate=21):
    """returns a pi_cam setup"""
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
