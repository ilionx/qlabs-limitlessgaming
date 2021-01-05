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

    def sound_with_window(self, sound, window=None):
        """
        return the sound when it's transformed with a hann window
        [Note: Performance]
        To optimise the performance as much as possible,
        it is recommended to always give window into the function.
        this prevents calculating the window over and over.

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
        >>> sound_with_window(size=3)
        array([0., 1., 0.])
        >>> sound_with_window(size=5)
        array([0., 0.5, 1., 0.5, 0.])
        >>> sound_with_window(size=10)
        array([0., 0.11697778, 0.41317591, 0.75, 0.96984631,
            0.96984631, 0.75, 0.41317591, 0.11697778, 0.])
        """

        if not window:
            window = Microphone.create_hann_window(size=len(sound))
        return sound * window

    def audio_to_fft(self, sound_array, samplerate=None, duration=None):
        """
        This function converts the audio data to FFT format

        Parameters
        ----------
        sound_array: array[float]
            a array with the sound signal, in Amplitude over time

        [OPTIONAL]
        samplerate: int
            a integer indicating the speed with which samples were taken

        [OPTIONAL]
        duration: int
            a integer indicating the duration, in seconds, for howlong samples were taken.

        Returns
        -------
        ret_arr : array[float]
            a array with the MFCC output of the FFT input

        Example
        -------
        >>> audio_to_fft(sound_array)
        array([])
        """
        if samplerate is None:
            samplerate = self.sample_rate
        if duration is None:
            duration = self.duration
        real_y = np.abs(rfft(sound_array))
        real_x = np.linspace(start=0, stop=samplerate//2,
                             num=(samplerate*duration)//2)
        if len(real_y) == max(len(real_x), len(real_y)):
            real_y = real_y[:len(real_x)]
        else:
            real_x = real_x[:len(real_y)]
        return real_y, real_x
