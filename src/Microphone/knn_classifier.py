"""a class to simplify and extend the KNN class from SKLearn"""
import os
import pickle

import soundfile as sf
from librosa import feature
from sklearn.neighbors import KNeighborsClassifier as KNC

def predict(knc_model: KNC, mfcc_sample: list):
    """returns a prediction from the given model"""
    return knc_model.predict([mfcc_sample])[0]

def save_model(model_to_save: KNC, filename: str):
    """Saves <model_to_save> to <filename> file for later reuse"""
    model_file = open(filename, "wb")
    pickle.dump(model_to_save, model_file)
    model_file.close()
def load_model(filename: str) -> KNC:
    """load an KNC model from <filename>"""
    model_file = open(filename, "rb")
    loaded_model = pickle.load(model_file)
    model_file.close()
    return loaded_model
def load_all_training_data(training_data_folder_name: str):
    """loads all data classified in with the name of the
    folder as the class, and the files as the examples"""
    os.chdir(training_data_folder_name)
    training_data = []
    folders = []
    for file_or_folder in os.listdir():
        if os.path.isdir(file_or_folder):
            folders.append(file_or_folder)
    for folder in folders:
        loaded_data = load_training_data(folder)
        training_data.append(loaded_data)
    os.chdir("..")
    return training_data
def split_data(data_to_split):
    """
    Split training data into classes and data
    Return
    ---
    classes, data
    """
    known_classes = []
    data_from_classes = []
    for i in data_to_split:
        known_classes.append(i[0])
        data_from_classes.append(i[1])
    return known_classes, data_from_classes
def reshape(mfcc, size: int):
    """reshapes a mfcc to a given size"""
    new_mfcc = []
    current_size = len(mfcc[0])
    factor = current_size // size
    for counter, arr in enumerate(mfcc):
        new_mfcc.append([])
        new_mfcc[counter] = list(arr[::factor])
        if size != len(new_mfcc[counter]):
            diff = len(new_mfcc[counter]) - size
            if diff % 2:
                diff -= 1
                diff = diff // 2
                if diff:
                    new_mfcc[counter] = new_mfcc[counter][diff:-(diff+1)]
                else:
                    new_mfcc[counter] = new_mfcc[counter][:-1]
            else:
                diff = diff // 2
                new_mfcc[counter] = new_mfcc[counter][diff:-diff]
    return new_mfcc
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
def transform_data(data_to_transform):
    """Transforms data_to_transform from a 2d array to a 1d array"""
    new_data = []
    for row in data_to_transform:
        new_data += list(row)
    return new_data
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
