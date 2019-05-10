import cv2
import numpy as np
from PIL import Image


def read(path: str):
    return Image.open(path)


def save(image, dest):
    try:
        image.save(dest)
    except:
        print("An error occured")


def to_numpy(image):
    return np.array(image)


def to_pillow(image):
    return Image.fromarray(image)


def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def to_blob(image):
    return cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)),
                                 1.0, (300, 300),
                                 (103.93, 116.77, 123.68))


def crop_box(path, box, size):
    image = read(path)
    return image.crop(box).resize(size)