import cv2
import os
import numpy as np
from PIL import Image
import pickle

def train_faces():
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(Base_dir, "images")

    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_id = {}
    y_labels = [] # it contains the label value
    x_train = [] # it contains the pixel value

    for root, dir, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpeg") or file.endswith("jpg"):
                path = os.path.join(root, file)

                # use any of the one
                # label = os.path.basename(root).replace(" ", "-").lower()
                label = os.path.basename(os.path.dirname(path)).replace(" ","_")
                # print(label, path)

                #creating id
                if not label in label_id:
                    label_id[label] = current_id
                    current_id += 1

                id_ = label_id[label]
                # print(label_id)

                # x_train.append(path)    # verify this image, turn into a numpy array, gray image
                # y_labels.append(label)  # some number of label

                # converting image into numpy array
                # convert image into numbers
                # and now we train the image_array
                pil_image = Image.open(path).convert("L") #grayscale

                # resizing images and the training
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, "uint8")
                # print(image_array)

                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                for(x, y, w, h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

    # print(y_labels)
    # print(x_train)

    with open("labels.pickle", 'wb') as f:
        pickle.dump(label_id, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainer.yml")
