import src.GPIO.rgb_led as rgb


class Status:
    """This class handles a status events for the system"""
    possible_states = (
        "Starting",
        "Idle",
        "Running",
        "Stopped",
        "Restarting"
    )
    status_codes = {
        "Starting": (0, 1, 0),
        "Idle": (0, 0, 1),
        "Running": (1, 1, 1),
        "Stopped": (1, 0, 0),
        "Restarting": (1, 0, 1)
    }

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

    def show(self):
        self.lights.light(self.status_codes[self.status])
