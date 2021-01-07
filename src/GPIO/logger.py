from time import time
from datetime import datetime


class Logger:
    """
    this class helps logging signals to the local file system

    Logger
    ===
    """

    def __init__(self, filename=None, time_format=None):
        if filename is None:
            self.filename = "log.csv"
        else:
            self.filename = filename
        if time_format is None:
            self.time_format = "unix"
        else:
            self.time_format = time_format

    def _log_raw(self, message):
        with open(self.filename, 'a') as log_file:
            log_file.write(time())
            log_file.write(message)
