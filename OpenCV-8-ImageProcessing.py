import cv2
import numpy as np
print(cv2.__version__)


kernel = np.ones((5,5),np.uint8)


img = cv2.imread('Resources/BlackPink.png')


img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)


imgCanny = cv2.Canny(img, 100, 100)


imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)


cv2.imshow('BlackPink',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dilate', imgDilation)


cv2.waitKey(0)