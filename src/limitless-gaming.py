"""The main file"""
import sys
from Camera.functions.open_face import *
from Camera.functions.pi_cam import *
from Camera.functions.my_functions import *
try:
    from GPIO.rgb_led import *
    from GPIO.switch import *
    GPIO_enabled = True
except ImportError as err:
    print(err)
    GPIO_enabled = False
from Microphone.knn_classifier import *
from Microphone.microphone import *

OPTIONS = {"cam": ["-c", "--camera"], "mic": ["-m", "--microphone"]}
SETTINGS = {"cam": False, "mic": False}

if __name__ == "__main__":
    for x in sys.argv:
        if x[0] == "-":
            for s in OPTIONS:
                if x in OPTIONS[s]:
                    SETTINGS[s] = True
    if SETTINGS["cam"]:
        input_stream = stream(detect=2, framerate=5)
        if GPIO_enabled:
            switches = MultiSwitchIn(19, 21, 23)
        FILMING = True
        while FILMING:
            FILMING, shoot, passen = next(input_stream)
            if GPIO_enabled:
                if shoot:
                    now = time.time()
                    led.On()
                elif passen:
                    led.Light(1, 0, 1)
                else:
                    led.Off()
                red, yellow, orange = switches.Check() # type: ignore

                print_on_current_line(
                    f"Red:{not red}, Yellow:{not yellow}, Orange:{not orange} time:{t()}")
                if not led.on:
                    led.Light(not red, not yellow, not orange)
    elif SETTINGS["mic"]:
        mic = Microphone()
        mic.stream()
