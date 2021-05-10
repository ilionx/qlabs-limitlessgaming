"""The main file"""
from config.config_manager import ConfigManager
from libs.util import debug, warning

system_config = ConfigManager()

USE_APP = system_config["interface"]["use"]
if USE_APP:
    from UI.server.app import app
    debug("Starting server")
    app.run(port=80)
    debug("Running server on \"http://localhost/\"")

USE_CAMERA = system_config["camera"]["use"]
if USE_CAMERA:
    from Camera.camera import Camera
    camera = Camera()

    USE_CAMERA_CONTOURS = system_config["camera"]["contours"]
    USE_CAMERA_OBJECTS = system_config["camera"]["objects"]
    if USE_CAMERA_CONTOURS:
        from Camera.scanner import ContourScanner
        contour_scanner = ContourScanner()
    if USE_CAMERA_OBJECTS:
        from Camera.scanner import CascadeScanner
        face_cascade_scanner = CascadeScanner(
            "./cascades/haarcascade_frontalface_default.xml")

USE_GPIO = system_config["gpio"]["use"]
if USE_GPIO:
    try:
        from GPIO.switch import MultiSwitchIn, MultiSwitchOut, SingleSwitchOut  # noqa # pylint: disable=unused-import
        from GPIO.logger import Logger  # noqa # pylint: disable=unused-import
        from GPIO.status import Status  # noqa # pylint: disable=unused-import
        from GPIO.rgb_led import RGBled  # noqa # pylint: disable=unused-import
    except Exception as e:
        warning("Could not import Jetson GPIO library")
        warning(e)

USE_MICROPHONE = system_config["microphone"]["use"]
if USE_MICROPHONE:
    from Microphone.microphone import Microphone
    microphone = Microphone()

if __name__ == "__main__":

    running = True
    while running:
        if USE_CAMERA and (USE_CAMERA_CONTOURS or USE_CAMERA_OBJECTS):
            frame = camera.read()
            if USE_CAMERA_CONTOURS:
                contours = contour_scanner.scan(frame)
            if USE_CAMERA_OBJECTS:
                objects = face_cascade_scanner.scan(frame)
        if USE_MICROPHONE:
            pass
        # TODO: handle triggers
