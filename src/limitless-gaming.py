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
    elif SETTINGS["mic"]:
