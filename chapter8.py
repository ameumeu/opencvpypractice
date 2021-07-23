import cv2
import numpy as np


def addStack(img1, img2):
    imgNew = np.hstack((img1, img2))

    return imgNew


def getContours(img):
    _, contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 3:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt, False)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, False)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                ObjectType = "Tri"
            else:
                ObjectType = "None"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, ObjectType,
                        (x+(w//2)-10, y+(h//2)-10), 0, 0.5, (0, 0, 0), 1)


img = cv2.imread("Resources/iu1.jpg")
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

imgStack = addStack(imgGray, imgBlur)
imgStack = addStack(imgStack, imgCanny)

cv2.imshow("horizontal", imgStack)
cv2.imshow("contours", imgContour)

cv2.waitKey(0)
