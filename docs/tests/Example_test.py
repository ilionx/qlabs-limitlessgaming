import unittest

# NOTE: the naming of a test should be as followed "test_<test_name>", e.g. "test_camera"
#       This is because of the workings of unittest, it'll scan for any methode starting with "test_"
class ExampleTests(unittest.TestCase):
    """A unittest with some simple test cases"""

    def test_success(self):
        """This test will succeed"""
        self.assertEqual(True, True)
        self.assertEqual("true".title(), "True")
        self.assertEqual(int(True), 1)

    def test_fail(self):
        """This test will fail"""
        self.assertEqual(True, False)
        self.assertEqual("true".title(), "False")
        self.assertEqual(int(True), 0)


if __name__ == "__main__":
    unittest.main()
