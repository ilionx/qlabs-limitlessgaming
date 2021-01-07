import src.GPIO.rgb_led as rgb


class Status:
    """This class handles a status events for the system"""
    def __init__(self, status=None):
        if status is None:
            self.status = "Starting"
        else:
            self.status = status
        self.lights = rgb.RGBled()

    def set_status(self, status):
        if status.title() in self.possible_states:
            self.status = status.title()
        else:
            raise Exception("Unknown status: %s" % status)

    def get_status(self):
        return self.status
