"""a class to simplify and extend the KNN class from SKLearn"""
import os
import pickle

import soundfile as sf
from librosa import feature
from sklearn.neighbors import KNeighborsClassifier as KNC

def predict(knc_model: KNC, mfcc_sample: list):
    """returns a prediction from the given model"""
    return knc_model.predict([mfcc_sample])[0]
