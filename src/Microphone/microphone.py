"""This module implements an microphone interface"""
import time as t

import numpy as np
import sounddevice as sd
from scipy.fft import rfft
