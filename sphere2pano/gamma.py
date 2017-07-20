import cv2
import sys
import numpy as np


def normalize(image):
    gamma = 1.5
    lookUpTable = np.zeros((256, 1), dtype='uint8')
    for i in range(256):
        lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    return cv2.LUT(image, lookUpTable)

image = cv2.imread(sys.argv[1])
image = cv2.copyMakeBorder(image, 5, 80, 30, 5,
                           cv2.BORDER_CONSTANT, value=[0, 0, 0])
image = cv2.fastNlMeansDenoising(image, None, 7, 7)
image = normalize(image)

cv2.imwrite(sys.argv[1] + '.gamma.png', image)
