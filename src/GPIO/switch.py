"""enables to use GPIO pins as output"""
import Jetson.GPIO as GPIO # type: ignore


class MultiSwitchIn:
    """This class is used to read multple switches as input"""

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        GPIO.setup(red, GPIO.IN)
        GPIO.setup(green, GPIO.IN)
        GPIO.setup(blue, GPIO.IN)

    def __del__(self):
        GPIO.cleanup((self.red, self.green, self.blue))

    def check(self):
        """checks the input of all the pins"""
        red = GPIO.input(self.red)
        green = GPIO.input(self.green)
        blue = GPIO.input(self.blue)
        return (red, green, blue)


class MultiSwitchOut:
    """This class is used to write multple switches as output"""

    def __init__(self, pins, invert=False, start=0):
        self.pin1 = pins[0]
        self.pin2 = pins[1]
        self.pin3 = pins[2]
        if start:
            start = GPIO.HIGH
        else:
            start = GPIO.LOW
        GPIO.setup(self.pin1, GPIO.OUT, initial=start)
        GPIO.setup(self.pin2, GPIO.OUT, initial=start)
        GPIO.setup(self.pin3, GPIO.OUT, initial=start)
        self.invert = invert

    def __del__(self):
        GPIO.cleanup((self.pin1, self.pin2, self.pin3))

    def send(self, pin1, pin2, pin3):
        """sends output to the corropsonding pins"""
        if self.invert:
            pin1 = not pin1
            pin2 = not pin2
            pin3 = not pin3
        if pin1:
            GPIO.output(self.pin1, GPIO.HIGH)
        else:
            GPIO.output(self.pin1, GPIO.LOW)
        if pin2:
            GPIO.output(self.pin2, GPIO.HIGH)
        else:
            GPIO.output(self.pin2, GPIO.LOW)
        if pin3:
            GPIO.output(self.pin3, GPIO.HIGH)
        else:
            GPIO.output(self.pin3, GPIO.LOW)


class SingleSwitchOut:
    """use a single pin on the GPIO board to send outputs from"""

    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup(self.pin)

    def send(self, pin):
        """send output to the pin"""
        if pin:
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)
