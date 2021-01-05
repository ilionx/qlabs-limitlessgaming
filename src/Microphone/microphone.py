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

    @staticmethod
    def create_hann_window(size=50):
        """
        Create a Hann window of the given size

        Parameters
        ----------
        size : int
            specifies the size of the returned array

        Returns
        -------
        arr : np.array[float]
            object with floating point numbers ranging between 0 and 1, and a size of `size`

        Example
        -------
        >>> create_Hann_window(size=3)
        array([0., 1., 0.])
        >>> create_Hann_window(size=5)
        array([0., 0.5, 1., 0.5, 0.])
        >>> create_Hann_window(size=10)
        array([0., 0.11697778, 0.41317591, 0.75, 0.96984631, 0.96984631,
            0.75, 0.41317591, 0.11697778, 0.])
        """
        arr = np.sin(np.linspace(-.5*np.pi, 1.5*np.pi, num=size))
        arr += 1
        arr /= 2
        return arr
