"""Used to manage a single RGB led, with the GPIO pins"""
import Jetson.GPIO as GPIO # type: ignore


class RGBled:
    """
    This class can manage 1 RGB led

    Attributes
    ----------
    red:int
        The pin number of the red common
    green:int
        The pin number of the green common
    blue:int
        The pin number of the blue common

    Methods
    -------
    cleanup()
        Cleans all the GPIO pins
    light(red, green, blue)
        Sets the light of the color to the corresponding value
    on()
        Turns on all the colors
    off()
        Turns off the light
    """

    def __init__(self, red=7, green=12, blue=15):
        print(f"using led:{red},{green},{blue}")
        self.red = red
        self.green = green
        self.blue = blue
        self.is_on = 0
        GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)

    def cleanup(self):
        """cleans the GPIO pins"""
        GPIO.cleanup((self.red, self.green, self.blue))

    def light(self, red: int, green: int, blue: int):
        """
        Sets the light of the color to the value

        Parameters
        ----------
        red:int
            0 for low, 1 for high
        green:int
            0 for low, 1 for high
        blue:int
            0 for low, 1 for high
        """
        self.is_on = (red or green or blue)
        if red:
            GPIO.output(self.red, GPIO.HIGH)
        else:
            GPIO.output(self.red, GPIO.LOW)
        if green:
            GPIO.output(self.green, GPIO.HIGH)
        else:
            GPIO.output(self.green, GPIO.LOW)
        if blue:
            GPIO.output(self.blue, GPIO.HIGH)
        else:
            GPIO.output(self.blue, GPIO.LOW)
    def on(self):
        """sets all the light on"""
        self.light(1, 1, 1)

    def off(self):
        """turns all the lights off"""
        self.light(0, 0, 0)
    def __del__(self):
        self.cleanup()

if __name__ == "__main__":
    import time
    GPIO.setmode(GPIO.BOARD)
    led = RGBled(7, 12, 15)
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(0.5)
    led.light(1, 0, 0)
    time.sleep(0.5)
    led.light(0, 1, 0)
    time.sleep(0.5)
    led.light(0, 0, 1)
    time.sleep(0.5)
    led.light(0, 1, 1)
    time.sleep(0.5)
    led.light(1, 1, 0)
    time.sleep(0.5)
    led.light(1, 0, 1)
    time.sleep(0.5)
    led.off()
    GPIO.cleanup()
