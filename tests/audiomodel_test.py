"""A simple testcase for the audio model classifier"""
import os
import sys
sys.path.insert(0, os.path.abspath('./src'))
import unittest

import Microphone.knn_classifier as KNC
from sklearn.neighbors import KNeighborsClassifier


class ModelTest(unittest.TestCase):
    """Test the data/models save and load functions"""
    MODEL_EXTENTION = ".knn-model"

    def test_load(self):
        """test the load function from KNC"""
        model = KNC.load_model(
            "./data/models/K-nearest neighbors/untrained.knn-model")
        self.assertEqual(type(model), type(
            KNeighborsClassifier(n_neighbors=1)), "ERROR(test_load): Wrong model loaded")

    def test_save(self):
        """Test the save function"""
        filename = "tests/assets/test_save"
        test_model = KNeighborsClassifier(n_neighbors=3)
        if not os.path.exists(filename+self.MODEL_EXTENTION):
            KNC.save_model(test_model, filename+self.MODEL_EXTENTION)
        else:
            no_file = True
            i = 1
            while no_file:
                if not os.path.exists(filename + str(i)+self.MODEL_EXTENTION):
                    filename = filename + str(i)
                    KNC.save_model(test_model, filename+self.MODEL_EXTENTION)
                    no_file = False
                else:
                    i += 1
        if not os.path.exists(filename+self.MODEL_EXTENTION):
            self.fail("Model was not saved to a file")

    def test_save_and_load(self):
        """Test the save and load methods from the KNC module"""
        filename = 'tests/assets/test_save_and_load'
        test_model = KNeighborsClassifier(n_neighbors=5)
        if not os.path.exists(filename+self.MODEL_EXTENTION):
            KNC.save_model(test_model, filename+self.MODEL_EXTENTION)
        else:
            no_file = True
            i = 1
            while no_file:
                if not os.path.exists(filename + str(i)+self.MODEL_EXTENTION):
                    filename = filename + str(i)
                    KNC.save_model(test_model, filename+self.MODEL_EXTENTION)
                    no_file = False
                else:
                    i += 1
        if not os.path.exists(filename+self.MODEL_EXTENTION):
            self.fail("No file was found")
        loaded_model = KNC.load_model(filename+self.MODEL_EXTENTION)
        self.assertEqual(type(test_model), type(loaded_model),
                         "ERROR(test_save_and_load): Wrong model loaded")
        self.assertEqual(test_model.__dict__, loaded_model.__dict__,
                         "ERROR(test_save_and_load): Models are not the same")

    def test_predict(self):
        """test the predict function from the KNC functions"""
        model = KNC.load_model(
            "./data/models/K-nearest neighbors/trained.knn-model")
        _, sound = KNC.load_training_file("./data/sounds/click.wav")
        transformed_sound = KNC.transform_data(sound)
        prediction = KNC.predict(model, transformed_sound)
        self.assertEqual(prediction, "clap",
                         "ERROR(test_predict): Wrong prediction")


if __name__ == "__main__":
    unittest.main()
