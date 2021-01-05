"""a class to simplify and extend the KNN class from SKLearn"""
import os
import pickle

import soundfile as sf
from librosa import feature
from sklearn.neighbors import KNeighborsClassifier as KNC

def predict(knc_model: KNC, mfcc_sample: list):
    """returns a prediction from the given model"""
    return knc_model.predict([mfcc_sample])[0]

def load_training_data(training_data_folder_name: str, ret_length=False):
    """loads training data from the given file name"""
    os.chdir(training_data_folder_name)
    files = []
    for file_or_folder in os.listdir():
        if os.path.isfile(file_or_folder):
            files.append(file_or_folder)
    sound_files = []
    for sound_file in files:
        file_data, samplerate = sf.read(sound_file)
        sound_files.append((file_data, samplerate))
    mfcc_data = []
    length = []
    for sound_data in sound_files:
        length.append(len(sound_data[0]))
        mfcc = feature.mfcc(
            sound_data[0], sr=sound_data[1], n_mfcc=25,
            hop_length=512, n_fft=2048)
        mfcc = reshape(mfcc, 20)
        mfcc_data.append(mfcc)
    os.chdir("..")
    if ret_length:
        return (training_data_folder_name, mfcc_data), length
    else:
        return (training_data_folder_name, mfcc_data)
def load_training_file(training_data_file_name: str, ret_length=False):
    """loads training data from the given file name"""
    file_data, samplerate = sf.read(training_data_file_name)
    length = len(file_data)
    mfcc = feature.mfcc(
        file_data, sr=samplerate, n_mfcc=25, hop_length=512, n_fft=2048)
    mfcc = reshape(mfcc, 20)
    if ret_length:
        return (training_data_file_name, mfcc), length
    else:
        return (training_data_file_name, mfcc)
def train_model(knc_model: KNC, training_data: list, training_classes: list):
    """trains a given model with given data"""
    known_classes = []
    new_data = []
    for i, training_class in enumerate(training_data):
        for training_data in training_class:
            known_classes.append(training_classes[i])
            transformed_data = transform_data(training_data)
            new_data.append(transformed_data)
    knc_model.fit(new_data, known_classes)
