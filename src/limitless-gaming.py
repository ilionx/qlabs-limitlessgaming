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

if __name__ == "__main__":
