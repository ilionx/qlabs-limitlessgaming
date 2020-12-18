"""A simple to for the audio model classifier"""
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
        self.fail("*** TODO: Create a test ***")

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
