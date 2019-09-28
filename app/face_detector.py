"""face detection module"""

import sys
import argparse

from typing import Any

from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
from matplotlib.patches import Rectangle

class FaceDetector(object):
    """Face Detection Helper Class"""

    def __init__(self):
        self.model = MTCNN()
        self._cache = {}

    def detect(self, image: Any = None, filename: str = None):
        if filename:
            image = pyplot.imread(filename)

        assert image, "No image found!"
        self._cache['input_image'] = image
        return self.model.detect_faces(image)

    def detect_and_draw(self, image: Any = None, filename: str = None):
        faces = self.detect(image=image, filename=filename)
        data = self._cache['input_image']
        pyplot.imshow(data)
        ax = pyplot.gca()
        for face in faces:
            x, y, width, height = face['box']
            rect = Rectangle((x, y), width, height, fill=False, color='red')
            ax.add_patch(rect)

        pyplot.show()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filename',
        action='store',
        required=True,
        help='name of the file in which faces are to be detected'
    )
    return parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    args = parse_arguments()
    detector = FaceDetector()
    print(detector.detect(args.filename))
    detector.detect_and_draw(args.filename)
