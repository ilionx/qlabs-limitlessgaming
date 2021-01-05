"""a class to simplify and extend the KNN class from SKLearn"""
import os
import pickle

import soundfile as sf
from librosa import feature
from sklearn.neighbors import KNeighborsClassifier as KNC

def predict(knc_model: KNC, mfcc_sample: list):
    """returns a prediction from the given model"""
    return knc_model.predict([mfcc_sample])[0]

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
