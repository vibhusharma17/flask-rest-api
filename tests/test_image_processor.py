import os
import unittest

from app.services.image_processor import ImageProcessor


class ImageProcessorTest(unittest.TestCase):

    def setUp(self):
        self.file_path = "{}/tests/data/test.jpg".format(os.path.abspath(os.getcwd()))
        self.invalid_path = "/abc/test.jpg"

    def test_perimeter_calculator(self):
        output = ImageProcessor.perimeter_calculator(self.file_path)
        self.assertTrue(int, type(output))

    def test_perimeter_calculator_raise_error(self):
        self.assertRaises(FileNotFoundError, ImageProcessor.perimeter_calculator, self.invalid_path)

    def test_remove_file(self):
        self.assertRaises(FileNotFoundError, ImageProcessor.remove_file, self.invalid_path)
