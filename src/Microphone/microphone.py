"""This module implements an microphone interface"""
import time as t

import numpy as np
import sounddevice as sd
from scipy.fft import rfft

class Microphone:
    """this class provides a simple interface to the Microphone"""

    def __init__(self, HOP_LENGTH=512, N_FFT=2048, SAMPLE_RATE=44100,
                 BLOCK_SIZE=1024, DURATION=3, THRESHOLD=0.1) -> None:
        self.hop_length = HOP_LENGTH
        self.n_fft = N_FFT
        self.sample_rate = SAMPLE_RATE
        self.block_size = BLOCK_SIZE
        self.duration = DURATION
        self.threshold = THRESHOLD
        self.list = []
        self.running = True
        self.start = None

