import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)

#print(img)
#img[:] = 255,0,0
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 100), (255, 0, 0), 2)
cv2.circle(img, (400, 50), 30, (0, 0, 255), 5)
cv2.putText(img, "Salve", (222, 149), cv2.FONT_ITALIC, 1, (255, 0, 0), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)