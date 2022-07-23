import cv2
import numpy as np
import pickle
import xlwt
from xlwt import Workbook
import datetime


def detectFaces():
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", 'rb') as f:
        labels = pickle.load(f)
        # inverting labels
        labels = {v:k for k,v in labels.items()}

    att = {}
    cap = cv2.VideoCapture(0)
    while True:
        # ret, frame = cap.read()
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,minNeighbors=5)

        for(x, y, w, h) in faces:
            # region of interset -> roi
            # print(x,y,w,h)

            # recoginze ? the roi
            # deep learned model keras, tensorflow, pytorch, scikit learm
            roi_gray = gray[y:y+h, x:x+w] #(y_cord_start, y_cord_end)
            roi_color = frame[y:y + h, x:x+w]


            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45: # and conf <= 85:
                # print(id_)
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                att[name] = id_

            # img_item = "my_image.png"
            # img_item1 = "my_color.png"
            # cv2.imwrite(img_item, roi_gray)
            # cv2.imwrite(img_item1, roi_color)

            color = (255, 0, 0) # not BGR -> Blue, Green, Red
            Stroke = 2 # thickness
            width = x+w # end_cord_x
            height = y+h # end_cord_y

            cv2.rectangle(frame, (x,y), (width, height), color, Stroke)
            # eyes = smile_cascade.detectMultiScale(roi_gray)
            #
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0),2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    lname = []
    for key in att.keys():
        lname.append(key)

    lname.sort()
    s = "S. No."
    n = "Name"
    sheet1.write(0, 0, s)
    sheet1.write(0, 1, n)
    for i in range(len(lname)):
        sheet1.write(i+1, 0 , i+1)
        sheet1.write(i+1, 1, lname[i])


    date = datetime.date.today()
    print(date)
    fileName = str(date)
    fileName += ".xls"


    wb.save(fileName)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return fileName

