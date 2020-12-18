"""Used to manage a single RGB led, with the GPIO pins"""
import Jetson.GPIO as GPIO # type: ignore


class RGBled:
    """this class can manage 1 RGB led"""

    def __init__(self, red: int, green: int, blue: int):
        print(f"using led:{red},{green},{blue}")
        self.red = red
        self.green = green
        self.blue = blue
        self.is_on = 0
        GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)

    def light(self, red: int, green: int, blue: int):
        """sets the light of the color to the value"""
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
