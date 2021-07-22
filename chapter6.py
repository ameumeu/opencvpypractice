import cv2
import numpy as np

img = cv2.imread("Resources/iu1.jpg")

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("horizontal", imgVer)

cv2.waitKey(0)
