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

    Datetime timeformat
    ---
    |Directive|Meaning|Example|
    |:---:|:---|---|
    |%a|Abbreviated weekday name.|Sun, Mon, ...|
    |%A|Full weekday name.|Sunday, Monday, ...|
    |%w|Weekday as a decimal number.|0, 1, ..., 6|
    |%d|Day of the month as a zero-padded decimal.|01, 02, ..., 31|
    |%-d|Day of the month as a decimal number.|1, 2, ..., 30|
    |%b|Abbreviated month name.|Jan, Feb, ..., Dec|
    |%B|Full month name.|January, February, ...|
    |%m|Month as a zero-padded decimal number.|01, 02, ..., 12|
    |%-m|Month as a decimal number.|1, 2, ..., 12|
    |%y|Year without century as a zero-padded decimal number.|00, 01, ..., 99|
    |%-y|Year without century as a decimal number.|0, 1, ..., 99|
    |%Y|Year with century as a decimal number.|2013, 2019 etc.|
    |%H|Hour (24-hour clock) as a zero-padded decimal number.|00, 01, ..., 23|
    |%-H|Hour (24-hour clock) as a decimal number.|0, 1, ..., 23|
    |%I|Hour (12-hour clock) as a zero-padded decimal number.|01, 02, ..., 12|
    |%-I|Hour (12-hour clock) as a decimal number.|1, 2, ... 12|
    |%p|Locale’s AM or PM.|AM, PM|
    |%M|Minute as a zero-padded decimal number.|00, 01, ..., 59|
    |%-M|Minute as a decimal number.|0, 1, ..., 59|
    |%S|Second as a zero-padded decimal number.|00, 01, ..., 59|
    |%-S|Second as a decimal number.|0, 1, ..., 59|
    |%f|Microsecond as a decimal number, zero-padded on the left.|000000 - 999999|
    |%z|UTC offset in the form +HHMM or -HHMM.| |
    |%Z|Time zone name.| |
    |%j|Day of the year as a zero-padded decimal number.|001, 002, ..., 366|
    |%-j|Day of the year as a decimal number.|1, 2, ..., 366|
    |%U|Week number of the year (Sunday as the first day of the week). |00, 01, ..., 53|
    |%W|Week number of the year (Monday as the first day of the week). |00, 01, ..., 53|
    |%c|Locale’s appropriate date and time representation.|Mon Sep 30 07:06:05 2013|
    |%x|Locale’s appropriate date representation.|09/30/13|
    |%X|Locale’s appropriate time representation.|07:06:05|
    |%%|A literal '%' character.|%|
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
        """
        Log a message with the Unix timestamp
        
        parameters
        ----------
        message:str
            a message to be logged, in unix format
        """
        with open(self.filename, 'a') as log_file:
            log_file.write(time())
            log_file.write(message)

    def _log_format(self, message):
        """
        Log a message with a custom datetime format
        
        parameters
        ----------
        message:str
            a message to be logged, in datetime format
        """
        with open(self.filename, 'a') as log_file:
            log_file.write(datetime.now().strftime(self.time_format))
            log_file.write(message)

    def log(self, message):
        """
        Public log method, this method determines if the time format is set
        
        parameters
        ----------
        message:str
            a string to be logged
        """
        if self.time_format == "unix":
            self._log_raw(message)
        else:
            self._log_format(message)
