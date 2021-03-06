from cactus.utils.image import (read, to_blob)
import cv2
import numpy as np

PROTOTXT = "../src/deploy.prototxt"
CAFFE_MODEL = "../src/res10_300x300_ssd_iter_140000.caffemodel"

SSD_NET = cv2.dnn.readNetFromCaffe(PROTOTXT, CAFFE_MODEL)


def dnn(imagen):
    img = read(imagen)
    img_width, img_height = img.size
    img_blob = to_blob(img)
    SSD_NET.setInput(img_blob)
    detections = SSD_NET.forward()
    boxes = list()

    for i in range(0, detections.shape[2]):
        confidense = detections[0, 0, i, 2]
        if confidense > 0.7:
            box = detections[0, 0, i, 3:7] * \
                np.array([img_width, img_height, img_width, img_height])
            boxes.append(box.astype('int'))
    return boxes
