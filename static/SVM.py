import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import joblib

classifier = joblib.load("/Users/dhanush/Documents/D/college/sem7/project/SVM/svm_model.pkl")

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)



offset = 20
imgSize = 300


labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L",
          "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",  "W", "X", "Y"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction = classifier.predict([imgWhite.reshape(-1)])
            print(prediction)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction = classifier.predict([imgWhite.reshape(-1)])

        cv2.rectangle(img, (x - offset, y - offset-50),
                      (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, prediction[0], (x, y - 26),
                    cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(img, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)
        
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
