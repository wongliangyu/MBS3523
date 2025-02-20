# Save this file to Github as OpenCV-20-YOLO-part3.py

import cv2
import numpy as np

confThreshold = 0.4

cap = cv2.VideoCapture(0)

classesFile = 'coco80.names'
classes = []
# Load all classes in coco80.names into classes[]
with open(classesFile, 'r') as f:
    classes = f.read().splitlines()
    print(classes)
    print(len(classes))

# Load the configuration and weights file
# You need to download the weights and cfg files from https://pjreddie.com/darknet/yolo/
net = cv2.dnn.readNetFromDarknet('yolov3-320.cfg','yolov3-320.weights')
# Use OpenCV as backend and use CPU
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


while True:
    success , img = cap.read()
    height, width, ch = img.shape

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()

    print(layerNames)

    output_layers_names = net.getUnconnectedOutLayersNames()
    #print(output_layers_names)

    LayerOutputs = net.forward(output_layers_names)
    print(len(LayerOutputs))
    # print(LayerOutputs[0].shape)
    # print(LayerOutputs[1].shape)
    # print(LayerOutputs[2].shape)
    #print(LayerOutputs[0][1])


    bboxes = [] # array for all bounding boxes of detected classes
    confidences = [] # array for all confidence values of matching detected classes
    class_ids = [] # array for all class IDs of matching detected classes

    for output in LayerOutputs:
        for detection in output:
            scores = detection[5:] # omit the first 5 values
            class_id = np.argmax(scores) # find the highest score ID out of 80 values which has the highest confidence value
            confidence = scores[class_id]
            if confidence > confThreshold:
                center_x = int(detection[0]*width) #YOLO predicts centers of image
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                bboxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
                #

    print(len(bboxes))
    indexes = cv2.dnn.NMSBoxes(bboxes, confidences, confThreshold,0.5) #Non-maximum suppresion
    print(indexes)
    print(indexes.flatten())
    #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    font = cv2.FONT_HERSHEY_PLAIN
    B, G, R = 150 , 0, 0

    if len(indexes) > 0:
        for i in indexes.flatten():
            x,y,w,h = bboxes[i]
            label = str(classes[class_ids[i]])
            if label == 'keyboard' or label == 'cell phone':
                confidence = str(round(confidences[i],2))
                cv2.rectangle(img,(x,y),(x+w,y+h),(B,G,R),2)
                cv2.putText(img,label+" "+ confidence,(x,y+20),font,1,(255,255,255),2)
                G = G+250

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()