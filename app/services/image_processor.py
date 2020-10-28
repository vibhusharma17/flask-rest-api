import os
from PIL import Image
from app.helpers.exception import FileNotFound


class ImageProcessor:
    """
    All the Image processing logic goes here.
    """
    results = []

    def __init__(self, filepaths):
        self.file_paths = []
        for path in filepaths:
            if os.path.exists(path):
                self.file_paths.append(path)
            else:
                raise FileNotFound("File not found.")

    @staticmethod
    def perimeter_calculator(file_path):
        image = Image.open(file_path)
        width, height = image.size
        perimeter = 2 * (height + width)
        return perimeter

    @staticmethod
    def remove_file(file_path):
        os.remove(file_path)
        return True

    def run(self):
        for path in self.file_paths:
            perimeter = self.perimeter_calculator(path)
            self.results.append(perimeter)
            self.remove_file(path)
        return self.results
