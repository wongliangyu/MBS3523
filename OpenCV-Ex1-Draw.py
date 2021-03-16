import cv2
print(cv2.__version__)
import numpy as np


img = np.zeros((500,500,3), np.uint8)
img = cv2.rectangle(img,(0,0),(500,500),(0,255,0),-1)


img = cv2.line(img,(0,250),(500,250),(0,0,255),5)

img = cv2.line(img,(250,0),(250,500),(0,0,255),5)


img = cv2.rectangle(img,(125,125),(375,375),(255,0,255),3)


img = cv2.circle(img,(125,125), 25, (128,0,128), 2)
img = cv2.circle(img,(375,125), 25, (128,0,128), 2)
img = cv2.circle(img,(125,375), 25, (128,0,128), 2)
img = cv2.circle(img,(375,375), 25, (128,0,128), 2)


cv2.imshow('img',img)

cv2.waitKey(0)