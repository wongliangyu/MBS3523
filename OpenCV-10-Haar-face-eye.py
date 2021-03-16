import cv2
import numpy as np
print(cv2.__version__)


faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')


img = cv2.imread('Resources/BlackPink.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(imgGray, 1.03, 5)


for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    roiImg = img[y:y+h, x:x+w]
    roiGray = imgGray[y:y+h, x:x+w]
    eyes = eyeCascade.detectMultiScale(roiGray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roiImg, (ex,ey), (ex+ew,ey+eh),(0,255,0),1)


cv2.imshow('Faces Detected',img)
cv2.waitKey(0)