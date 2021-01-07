import src.GPIO.rgb_led as rgb


class Status:
    """This class handles a status events for the system"""
    def __init__(self, status=None):
        if status is None:
            self.status = "Starting"
        else:
            self.status = status
        self.lights = rgb.RGBled()
