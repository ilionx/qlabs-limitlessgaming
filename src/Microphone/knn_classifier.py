"""a class to simplify and extend the KNN class from SKLearn"""
import os
import pickle

import soundfile as sf
from librosa import feature
from sklearn.neighbors import KNeighborsClassifier as KNC
