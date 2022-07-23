import numpy as np
import cv2

def Capture_images():
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)
    Id=input('enter your File Name: ')
    sampleNum=30
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for(x, y, w, h) in faces:
            print(x,y,w,h)
            #roi_gray = gray[y:y+h, x:x+w]
            #img_item = "9.png"
            #cv2.imwrite(img_item, roi_gray)

            sampleNum=sampleNum+1
            fileName = "C:\\Users\\DELL\\FaceRecoginition\\venv\\images\\{}\\".format(Id)
            # cv2.imwrite(fileName+Id+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imwrite(fileName + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        elif sampleNum>40:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
