import GPIO.rgb_led as rgb


class Status:
    """
    This class handles a status events for the system

    Attributes
    ----------
    possible_states:tuple
        all the possible states of the device
    status_codes:tuple
        a conversion from `status:str` to `status:(int,int,int)`
    status
        the current state of the device

    Methods
    -------
    set_status(status)
        sets the state of the device to `status`
    get_status()
        returns the current state of the device
    show()
        show the state of the device
    """
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
        """
        sets the state of the device to `status`

        parameters
        ----------
        status: str
            the new state of the device
        """
        if status.title() in self.possible_states:
            self.status = status.title()
        else:
            raise Exception("Unknown state: %s" % status)

    def get_status(self):
        """
        return the state of the device

        Returns
        -------
        str
            this is the state of the device
        """
        return self.status

    def show(self):
        """uses the RGB light to communicate the state of the device"""
        self.lights.light(self.status_codes[self.status])
