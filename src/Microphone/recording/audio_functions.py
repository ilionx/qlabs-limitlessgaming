"""A set of functions which are useful for working with sound"""
import numpy as np
import soundfile as sf
import pickle
import matplotlib.pyplot as plt
import sounddevice as sd


def tone_generater(duration, sample_rate, freq):
    """
    generate a single clear tone

    Parameters
    ----------
    duration: int
        the duration in seconds to generate the tone
    sample_rate:int
    freq:int

    Returns
    -------
    tone:np.array[float]
        a array of float values representing a tone

    Example
    -------
    >>> tone_generater(0.02, 44100, 250)                         
    array([ 0.00000000e+00,  3.56114331e-02,  7.11776904e-02,  1.06653653e-01,
        ...
        -7.11776904e-02, -3.56114331e-02])
    """
    if duration is None or sample_rate is None or freq is None:
        raise Exception(
            "Expected configuration, got duration:{}, sample_rate:{}, freq:{}".
            format(duration, sample_rate, freq))
    time = np.arange(int(np.ceil(duration * sample_rate))) / sample_rate
    return np.sin(2*np.pi * time * freq)


def multi_tone_generater(duration, sample_rate, frequencies, raw=False):
    """
    generate a multi-tone

    Parameters
    ----------
    duration: int
        the duration in seconds
    sample_rate:int
        the number of data points to generate per second
    frequencies:list
        a list of frequencies to combine
    raw:bool
        a indicator, this will also return the raw tone format(before summation)

    Returns
    -------
    muliple tones:np.array[float]
        a array with muliple tones combined

    Example
    -------
    >>> multi_tone_generater(0.02, 44100, [100, 1000, 400, 250])
    array([ 0.00000000e+00,  2.48812353e-01,  4.94514167e-01,  7.34053874e-01,
        ...
        -4.94514167e-01, -2.48812353e-01])
    """
    if duration is None or sample_rate is None or frequencies is None:
        raise Exception(
            "Expected configuration, got duration:{}, sample_rate:{}, freq:{}".
            format(duration, sample_rate, frequencies))
    tone = [tone_generater(duration, sample_rate, i) for i in frequencies]
    if raw:
        return sum(tone), tone
    return sum(tone)


def save_sound(filename, sound, sample_rate):
    """save a sound to a file"""
    sf.write(file=filename, data=sound, samplerate=sample_rate)


def save_plot(filename, plot):
    """save a plot to a file"""
    target = open(filename, "wb")
    pickle.dump(plot, target)


def load_plot(filename):
    """load a plot from a file"""
    return pickle.load(open(filename, "rb"))


def record_sound(duration, sample_rate):
    """record a sound for a given duration"""
    recording = sd.rec(int(duration*sample_rate),
                       samplerate=sample_rate, channels=1)
    sd.wait()
    return recording


def print_volume_bar(indata, *_args):
    """this function is called everytime a new block of sound is recorded"""
    volume_norm = np.linalg.norm(indata)*10
    print("|"*int(volume_norm), end=" " * (150-int(volume_norm)) + "\r")


if __name__ == "__main__":
    input_frequencies = [100, 1000, 400, 250]
    sound, sounds = multi_tone_generater(
        0.02, 44100, input_frequencies, raw=True)
    fig, axs = plt.subplots(len(sounds)+1)
    for i, x in enumerate(sounds):
        axs[i].plot(x)
        axs[i].set_title(str(input_frequencies[i]))
    axs[len(sounds)].plot(sound)
    axs[len(sounds)].set_title("+".join([str(x) for x in input_frequencies]))
    plt.show()
