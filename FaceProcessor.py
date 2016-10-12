from collections import Counter

import cv2
import numpy as np

from FaceRecognizer import Recognizer
from FaceRecognizerWindow import FaceRecognizerWindow

from PyQt4 import QtGui

file = 'learnedData.yml'
faceRecognizer = Recognizer(file)


def recognizeFace(predictedFace):
    predictedFace.value = None
    photos = readFrames("Test", 4, 2)
    print photos
    if len(photos) != 0:
        predicted = faceRecognizer.predict(photos)
        data = Counter(predicted)
        print "Predicted", data.most_common(1)[0][0]
        predictedFace.value = data.most_common(1)[0][0]
    cv2.destroyAllWindows()
    return predictedFace


def trainForFace(label):
    photos = readFrames("Train", 8, 2)
    labels = [label for i in range(len(photos))]
    faceRecognizer.update(photos, labels)
    cv2.destroyAllWindows()
    print "captured and trained for => " + str(labels)


def readFrames(Title, numberOfFrames, delay):
    app = QtGui.QApplication([Title])
    photos = []
    w = FaceRecognizerWindow(photos, numberOfFrames, delay, None)
    w.setWindowTitle(Title)
    w.show()
    app.exec_()
    return photos