from time import time
from datetime import datetime


class Logger:
    """
    this class helps logging signals to the local file system

    Logger
    ===
    By default the log files name is `log.txt`

    another file can be used, it's plain text format  


    By default the time format is the unix method, the amount of seconds since the epoch  

    for another format the python datetime format is used instead.  
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

    def log(self, message):
        if self.time_format == "unix":
            self._log_raw(message)
        else:
            with open(self.filename, "a") as log_file:
                log_file.write(datetime.now().strftime())
                log_file.write(message)
