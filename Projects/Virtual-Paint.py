import cv2
import numpy as np

frameWidth=640
frameHeight=480
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(3,frameHeight)
cap.set(10,150)

myColors=[[5,107,0,19,255,255],
          [133,56,0,159,156,255],
          [57,76,0,100,255,255],
          [94,103,117,179,255,255]]


def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        getContours(mask)
        # cv2.imshow(str(color[0]),mask)
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, [255, 0, 0], 3)
            peri=cv2.arcLength(cnt,True)
            approx= cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

while True:
    sucess,img=cap.read()
    imgResult = img.copy()
    findColor(img)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break