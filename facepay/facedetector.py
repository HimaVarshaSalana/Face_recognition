
import os
from django.urls import path, include
import face_recognition
import cv2 
from PIL import Image #?


#initialize the camera
def facedect(loc):
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:   
            # frame captured without any errors
            cv2.namedWindow("image_test")
            cv2.imshow("image_test",img)
            #cv2.waitKey(0) # waits until a key is pressed
            cv2.destroyWindow("image_test")
            cv2.imwrite("captured-image.png",img) #to save the captured image to the directory file

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_ROOT =os.path.join(BASE_DIR,'aps_site')

            print(MEDIA_ROOT,loc)
            loc=(str(MEDIA_ROOT)+loc)
            print(loc)
            print("E:\paybyface\images")
            face_1_image = face_recognition.load_image_file(loc)
            face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

            small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)

            print(check)
            if check[0]:
                    return True

            else :
                    return False    

facedect('E:\paybyface\media\face_id')")
