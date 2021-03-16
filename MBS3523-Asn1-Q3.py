import cv2
import numpy as np
carcascde = cv2.CascadeClassifier('Resources/cars3.xml')
pedcascde=cv2.CascadeClassifier('Resources/haarcascade_fullbody.xml')
capture=cv2.VideoCapture('Resources/a_VrvfF51CDGgN1609164950_10s_v1.mp4')
capture.set(3,640)
capture.set(3,480)

while True:
    success, img=capture.read()
    imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car=carcascde.detectMultiScale(imGray,1.1,5)
    for(x,y,w,h)in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
    ped=pedcascde.detectMultiScale(imGray,1.1,1)
    for(x,y,w,h)in ped:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
    cv2.imshow('car',img)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()