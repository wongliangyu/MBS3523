import cv2
import random
import numpy as np
capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)
dxy=[-1,1]
x=0
dx=1
y=0
dy=1
b=g=r=0
while True:
    success, img=capture.read()
    cv2.rectangle(img,(x,y),(x+80,y+80),(b,g,r),3)
    x=x+dx
    y=y+dy
    if x<=0 or y<=0 or x>=560 or y>=400:
        db=random.randint(0,1)
        dg = random.randint(0, 1)
        dr = random.randint(0, 1)
        d=random.randint(-2,2)
        f=random.randint(-2,2)
        b=255*db
        g=255*dg
        r=255*dr
        dx = 1 * d
        dy = 1 * f
        if  x<0:
            dx=1
            x=1
        elif y<0:
            dy=1
            y=1
        elif x>560:
            dx=-1
            x=559
        elif y>400:
            dy=-1
            y=399
    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()