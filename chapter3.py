import cv2
import numpy as np

img = cv2.imread("Resources/iu1.jpg")

imgResize = cv2.resize(img, (633, 960))

imgCropped = img[500:700, 300:800]

cv2.imshow("IU", imgCropped)


cv2.waitKey(0)
