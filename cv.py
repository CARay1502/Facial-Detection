#written by Christian Ray 
import os 
#this code snippit pulled from reddit
#this disables microsoft msmf image processing
#allows camera feed to open faster without extra processing 
#include if your webcam or other video feed is slow to load
#"0" is false value for MSMF- NOT your video input value
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

#haarcascades xml file for faces -> identify faces with pretrained data
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# open web cam - 0 default input
#if there are issues in displaying a video feed
#check your devices video input options to identify correct input value
#0 is usually default
cap = cv2.VideoCapture(0)

#error handling to identify correct video capture 
if (cap.isOpened()== False):
    print('Error')

#while loop to run program through each frame instantly 
while True:
    #this takes individual frames from web cam - cap.read()
    ret, frame = cap.read()
    if not ret:
        break

    #converts frames with a gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces from haarcascades with gray(frame -> cap)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    #draws rectangle around detected faces ->cv2.rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #displays frame and processed video feed
    cv2.imshow('Face Detection', frame)

        #binds break program func to q keybind
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break    

#ends program after while loop has been broken from keybind func
cap.release()
cv2.destroyAllWindows()
