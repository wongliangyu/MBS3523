import cv2
print(cv2.__version__)
import numpy as np


img = np.zeros((500,500,3), np.uint8)


img = cv2.line(img,(0,0),(500,500),(255,0,0),5)


img = cv2.circle(img,(400,100), 50, (0,0,255), -1)


img = cv2.rectangle(img,(250,0),(500,125),(0,255,0),3)


img = cv2.ellipse(img,(250,250),(100,50),0,0,180,(125,255,255),-1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('img',img)

cv2.waitKey(0)