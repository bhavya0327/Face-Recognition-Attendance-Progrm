import CapturingImages
import Path
import FaceDetection
import Emailautomation
import FaceTrain
import os

print("Press 1 for new Entry")
print("Press 2 for Capture Images")
print("Press 3 for Train Images")
print("Press 4 for Detecting Face amd Sending Email")
print("Press 5 for Exit")

def main():
    while True:
        try:
            n = int(input("Enter your choice: "))

            if n == 1:
                newDirectory()

            elif n == 2:
                capture()

            elif n == 3:
                train()

            elif n == 4:
                detect()

            elif n == 5:
                print("Thank You")
                break

            else:
                print("Invalid Choice. Enter 1-4")
                Main()

        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")


# ************************* Making new Directory **************************************
def newDirectory():
    pathName = input("Enter the folder name: ")
    Path.makeNewDirectory(pathName)
    key = input("Enter any key to return main menu: ")
    main()


# ************************ Capturing faces ********************************************
def capture():
    CapturingImages.Capture_images()
    key = input("Enter any key to return main menu: ")
    main()


# *********************** Training faces ***********************************************
def train():
    FaceTrain.train_faces()
    key = input("Enter any key to return main menu: ")
    main()


# ********************** Detecting Faces ***********************************************
def detect():
    fileName = FaceDetection.detectFaces()
    key = input("Enter any key to return main menu: ")

    ans = input("If you want to send mail press y: ")
    if ans == 'y':
        mail(fileName)
    main()


# ********************* Sending Mail ***************************************************
def mail(fileName):
    s = input("Enter your email id: ")
    Emailautomation.sendingEmail(s, fileName)
    key = input("Enter any key to return main menu: ")
    main()

if __name__ == "__main__":
    main()
