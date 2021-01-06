"""A simple testcase for the audio model classifier"""
import os
import unittest

import src.Microphone.knn_classifier as KNC
from sklearn.neighbors import KNeighborsClassifier


class ModelTest(unittest.TestCase):
    """Test the data/models save and load functions"""

    def test_load(self):
        """test the load function from KNC"""
        model = KNC.load_model(
            "./data/models/K-nearest neighbors/untrained.knn-model")
        self.assertEqual(type(model), type(
            KNeighborsClassifier(n_neighbors=1)))

    def test_save(self):
        """Test the save function"""
        filename = "tests/assets/test_save.knn-model"
        test_model = KNeighborsClassifier(n_neighbors=3)
        if not os.path.exists(filename):
            KNC.save_model(test_model, filename)
        else:
            no_file = True
            i = 1
            while no_file:
                if not os.path.exists(filename + str(i)):
                    filename = filename + str(i)
                    KNC.save_model(test_model, filename)
                    no_file = False
                else:
                    i += 1
        if not os.path.exists(filename):
            self.fail("Model was not saved to a file")

    def test_save_and_load(self):
        """Test the save and load methods from the KNC module"""
        filename = 'tests/assets/test_save_and_load.knn-model'
        test_model = KNeighborsClassifier(n_neighbors=5)
        if not os.path.exists(filename):
            KNC.save_model(test_model, filename)
        else:
            no_file = True
            i = 1
            while no_file:
                if not os.path.exists(filename + str(i)):
                    filename = filename + str(i)
                    KNC.save_model(test_model, filename)
                    no_file = False
                else:
                    i += 1
        if not os.path.exists(filename):
            self.fail("No file was found")
        loaded_model = KNC.load_model(filename)
        self.assertEqual(type(test_model), type(loaded_model))
        self.assertEqual(test_model.__dict__, loaded_model.__dict__)

    def test_predict(self):
        """test the prdict function from the KNC functions"""
        model = KNC.load_model(
            "./data/models/K-nearest neighbors/trained.knn-model")
        _, sound = KNC.load_training_file("./data/sounds/click.wav")
        transformed_sound = KNC.transform_data(sound)
        prediction = KNC.predict(model, transformed_sound)
        self.assertEqual(prediction, "clap")


if __name__ == "__main__":
    unittest.main()
