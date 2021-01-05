"""A set of functions which are useful for working with sound"""
import numpy as np
import soundfile as sf
import pickle
import matplotlib.pyplot as plt
import sounddevice as sd


def tone_generater(duration, sample_rate, freq):
    """generate a single clear tone"""
    if duration is None or sample_rate is None or freq is None:
        raise Exception(
            "Expected configuration, got duration:{}, sample_rate:{}, freq:{}".
            format(duration, sample_rate, freq))
    time = np.arange(int(np.ceil(duration * sample_rate))) / sample_rate
    return np.sin(2*np.pi * time * freq)


def multi_tone_generater(duration, sample_rate, freqs, raw=False):
    """generate a multi-tone"""
    if duration is None or sample_rate is None or freqs is None:
        raise Exception(
            "Expected configuration, got duration:{}, sample_rate:{}, freq:{}".
            format(duration, sample_rate, freqs))
    tone = [tone_generater(duration, sample_rate, i) for i in freqs]
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
    input_freqs = [100, 1000, 400, 250]
    sound, sounds = multi_tone_generater(0.02, 44100, input_freqs, raw=True)
    fig, axs = plt.subplots(len(sounds)+1)
    for i, x in enumerate(sounds):
        axs[i].plot(x)
        axs[i].set_title(str(input_freqs[i]))
    axs[len(sounds)].plot(sound)
    axs[len(sounds)].set_title("+".join([str(x) for x in input_freqs]))
    plt.show()
