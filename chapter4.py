import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
#img[:] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 10)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (0, 0), 30, (255, 255, 0), cv2.FILLED)
cv2.putText(img, " Some things never change ", (200, 300),
            cv2.FONT_HERSHEY_COMPLEX, q1, (255, 94, 255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
