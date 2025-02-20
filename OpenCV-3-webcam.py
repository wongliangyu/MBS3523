import cv2
import numpy as np
print(cv2.__version__)


capture = cv2.VideoCapture(0)

capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame

while True:
    success, img = capture.read()

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()